from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sender_info = fields.Text('Yuboruvchi Malumotlari')
    recipient_info = fields.Text('Qabul Qilib Oluvchi Malumotlari')
    sender_branch = fields.Many2one('res.branch', 'Yuboruvchi Fliial')
    recipient_branch = fields.Many2one('res.branch', 'Qabul Qilib Oluvchi Fliial')
    shipping_cost = fields.Float('Shipping Cost', compute='_compute_shipping_cost')
    total_amount = fields.Float('Total Amount', compute='_compute_total_amount')
    product_info = fields.One2many('sale.order.product', 'order_id', 'Mahsulot Malumotlari')

    @api.depends('product_info')
    def _compute_shipping_cost(self):
        for order in self:
            shipping_cost = 0
            for line in order.product_info:
                if line.weight <= 1:
                    shipping_cost += 15000
                elif line.weight <= 5:
                    shipping_cost += 15000 + (line.weight - 1) * 1000
                elif line.weight <= 30:
                    shipping_cost += 15000 + (line.weight - 1) * 2000
                else:
                    shipping_cost += 15000 + (line.weight - 1) * 2000 + 30000
                if line.volume > 1:
                    shipping_cost += 30000
                if line.fragile:
                    shipping_cost += 5000
            order.shipping_cost = shipping_cost

    @api.depends('product_info', 'partner_id.loyalty_points')
    def _compute_total_amount(self):
        for order in self:
            total_amount = order.amount_total
            if order.partner_id.loyalty_points >= 100:
                total_amount -= total_amount * 0.05
            elif order.partner_id.loyalty_points >= 500:
                total_amount -= total_amount * 0.10
            elif order.partner_id.loyalty_points >= 1000:
                total_amount -= total_amount * 0.15
            order.total_amount = total_amount


class SaleOrderProduct(models.Model):
    _name = 'sale.order.product'
    _description = 'Sale Order Product'

    order_id = fields.Many2one('sale.order', string='Order')
    product_id = fields.Many2one('product.product', string='Product')
    package_count = fields.Integer(string='Package Count', required='product_id.package_count')
    weight = fields.Float(string='Weight', required='product_id.weight')
    volume = fields.Float(string='Volume', required='product_id.volume')
    fragile = fields.Boolean(string='Fragile', required='product_id.fragile')
