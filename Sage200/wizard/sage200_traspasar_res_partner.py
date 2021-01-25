# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _

class Sage200Traspasar(models.TransientModel):
    _name = "sage200.traspasar.res.partner"
    _description = "Traspasar Contacto a Sage200"



    def set_send_sage200(self):
        self.ensure_one()                   #Sólo se ejecuta para un registro (Desde el formulario)
        active_id=self.env.context.get('active_id')
        active_model=self.env.context.get('active_model')
        if active_id and active_model and active_model=='res.partner':
            partner = self.env['res.partner'].browse(active_id)
            partner.traspasarSage200="pending"
