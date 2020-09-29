# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountBankStatementLine(models.Model):
    _name = "account.bank.statement.line"
    _inherit = "account.bank.statement.line"

    from_existing = fields.Boolean(
        string="From Existing Entry",
        default=False,
    )
