# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class AccountBankStatementLine(models.Model):
    _name = "account.bank.statement.line"
    _inherit = "account.bank.statement.line"

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
