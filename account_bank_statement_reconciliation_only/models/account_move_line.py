# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class AccountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = "account.move.line"

    @api.multi
    def _get_amount_for_statement_line(self):
        self.ensure_one()
        if self.debit > 0.0:
            return self.debit
        else:
            return -1.0 * self.credit

    @api.multi
    def prepare_bank_statement_line(self):
        self.ensure_one()
        return {
            "name": self.name,
            "date": self.move_id.date,
            "amount": self._get_amount_for_statement_line(),
            "partner_id": self.partner_id and self.partner_id.id or False,
            "bank_account_id": False,  # TODO
            "account_id": self.account_id.id,
            "ref": self.move_id.name,
            "journal_entry_id": self.move_id.id,
        }
