# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class AccountBankStatement(models.Model):
    _name = "account.bank.statement"
    _inherit = "account.bank.statement"

    @api.depends(
        "balance_end_real",
    )
    @api.multi
    def _compute_replenish_amount(self):
        for document in self:
            replenishment_amount = 0.0
            if document.journal_id:
                journal = document.journal_id
                replenishment_amount = (
                    journal.replenishment_limit - document.balance_end_real
                )
            document.replenish_amount = replenishment_amount

    replenish_amount = fields.Float(
        string="Replenishment Amount",
        compute="_compute_replenish_amount",
        store=True,
    )
