# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountBankStatement(models.Model):
    _name = "account.bank.statement"
    _inherit = [
        "account.bank.statement",
        "mixin.policy",
    ]

    @api.multi
    def _compute_policy(self):
        _super = super(AccountBankStatement, self)
        _super._compute_policy()

    # Policy Field
    reconcile_ok = fields.Boolean(
        string="Can Reconcile",
        compute="_compute_policy",
    )
    validate_ok = fields.Boolean(
        string="Can Validate",
        compute="_compute_policy",
    )
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
    )
    approve_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
    )
    reject_ok = fields.Boolean(
        string="Can Reject",
        compute="_compute_policy",
    )

    @api.onchange(
        "journal_id",
    )
    def onchange_policy_template_id(self):
        template_id = self._get_template_id()
        for document in self:
            document.policy_template_id = template_id
