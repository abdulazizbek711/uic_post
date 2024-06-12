from odoo import models, fields, api
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    shipping_status = fields.Selection([
        ('draft', 'Draft'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered')
    ], string='Shipping Status')

    @api.model
    def _process_picking(self):
        for picking in self:
            if picking.state == 'draft':
                picking.state = 'in_transit'