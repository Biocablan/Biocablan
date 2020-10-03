# Copyright 2020 Raul Carbonell - raul.carbonell@processcontrol.es
# License AGPL-3.0 or later
{
    "name": "EDI - Odoo",
    "summary":
        "Enlace con Ediversa",
    "version": "13.0.1.0.0",
    "category": "Sales",
    "website": "",
    "author": "Raul Carbonell",
    "license": "AGPL-3",
    "data": [
        "scheduler.xml",
        'views/views.xml',
    ],
    "depends": [
        "crm",
        "sale"
    ],
    "application": True,
    "installable": True,
}
