from odoo import http
from odoo.http import request

class OrderStatusController(http.Controller):
    @http.route('/order-status', type='http', auth='public', website=True)
    def order_status_input(self, **kwargs):
        return http.request.render('uic_post.order_status_input_template')

    @http.route('/order-info', type='http', auth='public', website=True)
    def order_status(self, **kwargs):
        order_id = int(kwargs.get('order_id'))
        order = request.env['sale.order'].sudo().browse(order_id)
        if order:
            return http.request.render('uic_post.order_status_template', {
                'order': order,
            })
        else:
            return http.request.render('uic_post.order_status_input_template', {'error': 'Wrong order ID, try again!'})