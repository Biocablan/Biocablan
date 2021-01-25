# Copyright 2020 Raul Carbonell - raul.carbonell@processcontrol.es
# License AGPL-3.0 or later
{
    "name": "Sincro Sage200-Odoo",
    "summary":
         "Sincro Sage200-Odoo",
    "version": "13.0.1.0.0",
    "category": "undefined",
    "website": "",
    "author": "Raul Carbonell",
    "license": "AGPL-3",
    "data": [
        "wizard/sage200_traspasar_res_partner_views.xml",
        "views/res_partner_views.xml",
        "views/res_company_views.xml",
    ],
    "depends": [
        "base",
        "crm", 
    ],
    "application": True,
    "installable": True,
}
