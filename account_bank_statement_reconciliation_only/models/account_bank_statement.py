# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AccountBankStatement(models.Model):
    _name = "account.bank.statement"
    _inherit = "account.bank.statement"

    @api.depends(
        "journal_id",
    )
    def _compute_reconciliation_only(self):
        for document in self:
            self.reconciliation_only = self.journal_id.reconciliation_only

    reconciliation_only = fields.Boolean(
        string="Reconciliation Only",
        compute="_compute_reconciliation_only",
        store=False,
    )
    date_end = fields.Date(
        string="Date End",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
            "open": [
                ("readonly", False),
            ],
        }
    )

    @api.multi
    def action_repopulate_transanction(self):
        for document in self:
            self._repopulate_transanction()

    @api.multi
    def _repopulate_transanction(self):
        self.ensure_one()
        self.line_ids.write({"journal_entry_id": False})
        self.line_ids.unlink()
        self.write({"line_ids": self._get_statement_lines_dict()})

    @api.multi
    def _get_statement_lines_dict(self):
        self.ensure_one()
        result = []
        obj_line = self.env["account.move.line"]
        criteria = [
            ("journal_id", "=", self.journal_id.id),
            ("account_id", "=", self.journal_id.default_debit_account_id.id),
            ("date", ">=", self.date),
            ("date", "<=", self.date_end),
        ]
        for line in obj_line.search(criteria):
            result.append((0, 0, line.prepare_bank_statement_line()))

        return result
