# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class AccountJournal(models.Model):
    _name = "account.journal"
    _inherit = "account.journal"

    replenishment_limit = fields.Float(
        string="Replenishment Limit",
        default=0.0,
    )
