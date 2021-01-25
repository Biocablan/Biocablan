# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


import logging
_logger=logging.getLogger(__name__)


class ResPartnerS200(models.Model):
    _inherit = "res.partner"



    is_tipo_potencial = fields.Boolean(string="Cliente Potencial", default=True, readonly=True )


    traspasarSage200 = fields.Selection(
        string="Traspasar a Sage 200",
        selection=[
                ('pending', 'Pending'),
                ('complete', 'Complete'),
        ],
    )

    def set_send_sage200(self):
        self.ensure_one()                   #Sólo se ejecuta para un registro (Desde el formulario)
        self.traspasarSage200="pending"


    @api.model
    def create(self, vals):
        #Al crear un contacto de una empresa que sea cliente, se marcará como pendiente para traspasar a Sage
        if vals.get('parent_id'):
            parentid=vals.get('parent_id')
            is_company=vals.get('is_company')
            type=vals.get('type')
            if type == "delivery":
                if parentid:
                    partner = self.env['res.partner'].browse(parentid)
                    if partner.codigoclientesage:
                        if is_company == False:
                            vals.update({'traspasarSage200':'pending'})

        res = super(ResPartnerS200, self).create(vals)

        return res
