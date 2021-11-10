# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountBankStatement(models.Model):
    _name = "account.bank.statement"
    _inherit = [
        "account.bank.statement",
        "mixin.multiple_approval",
    ]
    _approval_from_state = "open"
    _approval_to_state = "confirm"
    _approval_state = "approval"

    state = fields.Selection(
        selection=[
            ("open", "New"),
            ("approval", "Waiting For Approval"),
            ("confirm", "Validated"),
            ("cancel", "Cancelled"),
            ("reject", "Rejected"),
        ]
    )

    def action_confirm(self):
        for document in self:
            document.write({"state": "approval"})
            document.action_request_approval()

    def action_restart(self):
        for document in self:
            document.write({"state": "open"})

    def action_cancel(self):
        for document in self:
            for line in document.line_ids:
                if line.journal_entry_ids:
                    line.button_cancel_reconciliation()
            document.write({"state": "cancel"})

    def action_approve_approval(self):
        _super = super(AccountBankStatement, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.check_confirm_bank()
                document.write({"state": "confirm"})

    def action_reject_approval(self):
        _super = super(AccountBankStatement, self)
        _super.action_reject_approval()
        for document in self:
            if document.rejected:
                for line in document.line_ids:
                    if line.journal_entry_ids:
                        line.button_cancel_reconciliation()
