from odoo import models, fields, api

class PromoCode(models.Model):
    _name = 'promo.code'
    _description = 'Promo Code'

    name = fields.Char('Code', required=True)
    discount = fields.Float('Discount (%)', required=True)
    active = fields.Boolean('Active', default=True)
    expiry_date = fields.Date('Expiry Date')
