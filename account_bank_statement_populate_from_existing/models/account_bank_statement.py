# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class AccountBankStatement(models.Model):
    _name = "account.bank.statement"
    _inherit = "account.bank.statement"

    @api.multi
    def action_populate_transanction(self):
        for document in self:
            document._populate_transanction()

    @api.multi
    def action_remove_transaction(self):
        for document in self:
            document._remove_transaction()

    @api.multi
    def _remove_transaction(self):
        self.ensure_one()
        self.line_ids.write({"journal_entry_id": False})
        self.line_ids.unlink()

    @api.multi
    def _populate_transanction(self):
        self.ensure_one()
        self._remove_transaction()
        self.write({"line_ids": self._get_statement_lines_dict()})

    @api.multi
    def _get_statement_lines_dict(self):
        self.ensure_one()
        result = []
        obj_line = self.env["account.move.line"]
        criteria = [
            ("journal_id", "=", self.journal_id.id),
            ("account_id", "=", self.journal_id.default_debit_account_id.id),
            ("date", "=", self.date),
            ("statement_id", "=", False),
        ]
        for line in obj_line.search(criteria):
            result.append((0, 0, line.prepare_bank_statement_line()))

        return result
