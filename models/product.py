from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    package_count = fields.Integer(string='Package Count')
    weight = fields.Float(string='Weight')
    volume = fields.Float(string='Volume')
    fragile = fields.Boolean(string='Fragile')
