# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _

class EdiSaleOrder(models.Model):
    _name="edi.sale.order"
    _description = 'EDI Sale Order'

    xml_base64 = fields.Char(string="XML Base64", )


    @api.model
    def sync_orders_ediversa_to_odoo(self):
        import http.client
        import mimetypes
        conn = http.client.HTTPSConnection("comedicloudwstest.ediversa.net", 9025)
        payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<soapenv:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\nxmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\nxmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\nxmlns:com=\"comedicloudws\">\r\n<soapenv:Header/>\r\n<soapenv:Body>\r\n<com:downloadDocumentList\r\nsoapenv:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\r\n<user xsi:type=\"xsd:string\">te2z000200</user>\r\n<password xsi:type=\"xsd:string\">NamuSamanda2020</password>\r\n</com:downloadDocumentList>\r\n</soapenv:Body>\r\n</soapenv:Envelope>"
        headers = {
            'content-Type': 'text/xml'
        }
        conn.request("POST", "/Server", payload, headers)
        res = conn.getresponse()
        data = res.read()
        respuesta=data.decode("utf-8")

        import xml.etree.ElementTree as ET
        root = ET.fromstring(respuesta)

        for child in root[0][0][0][1]:
            print(child.text)
