# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Bank Statement - Workflow Policy",
    "version": "11.0.1.1.0",
    "category": "Administration",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "account_bank_statement_multiple_approval",
        "ssi_policy_mixin",
    ],
    "data": [
        "data/policy_template_data.xml",
        "views/account_bank_statement_view.xml",
    ],
}
