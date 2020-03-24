# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountJournal(models.Model):
    _name = "account.journal"
    _inherit = "account.journal"

    reconciliation_only = fields.Boolean(
        string="Reconciliation Only",
        default=False,
    )
