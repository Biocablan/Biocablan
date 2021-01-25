# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class ResCompanySage200(models.Model):
    _inherit = "res.company"

    codigosage = fields.Integer(string="Código Empresa Sage", )
