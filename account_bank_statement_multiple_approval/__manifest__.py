# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Bank Statement Multiple Approval",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "category": "Accounting",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "depends": [
        "account_cancel",
        "ssi_multiple_approval_mixin",
    ],
    "data": [
        "views/account_bank_statement_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "auto_install": False,
}
