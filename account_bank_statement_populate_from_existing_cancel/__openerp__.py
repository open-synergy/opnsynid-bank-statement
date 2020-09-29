# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Populate Bank Statement & Cash Register from Existing Entry - "
            " Cancel",
    "version": "8.0.1.0.0",
    "category": "Accounting",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "account_bank_statement_populate_from_existing",
        "account_cancel",
    ],
    "data": [
        "views/account_bank_statement_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
