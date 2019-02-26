from odoo import models, fields, api

class order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'


    cara_bayar = fields.Char("Cara Bayar")

    purchase_id = fields.Many2one(comodel_name="purchase.order",string="PO")

    location_ids = fields.One2many(comodel_name="sale.order.location",
                                    inverse_name="sale_id",
                                    string="Qty per Locations", required=False, )

    @api.multi
    def action_confirm(self):
        res = super(order, self).action_confirm()

        if 'Cash' in self.partner_id.category_id.mapped('name'):
            self.cara_bayar = 'Tunai'
        elif 'Bank' in self.partner_id.category_id.mapped('name'):
            self.cara_bayar = 'Bank'

        return res


class sale_location(models.Model):
    _name = 'sale.order.location'

    sale_id = fields.Many2one(comodel_name="sale.order", string="SO", required=False, )
    location_id = fields.Many2one(comodel_name="stock.location", string="Location", required=False, )
    quantity = fields.Float(string="Quantity",  required=False, )