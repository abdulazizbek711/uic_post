from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_points = fields.Integer(string='Loyalty Points', default=0)
    loyalty_discount = fields.Float(string='Loyalty Discount', compute='_compute_loyalty_discount')

    def _compute_loyalty_discount(self):
        for partner in self:
            if partner.loyalty_points >= 1000:
                partner.loyalty_discount = 15
            elif partner.loyalty_points >= 500:
                partner.loyalty_discount = 10
            elif partner.loyalty_points >= 100:
                partner.loyalty_discount = 5
            else:
                partner.loyalty_discount = 0