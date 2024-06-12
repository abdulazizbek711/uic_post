from odoo import models, fields

class ResBranch(models.Model):
    _name = 'res.branch'
    _description = 'Branch'

    name = fields.Selection([
        ('andijan', 'Andijan'),
        ('bukhara', 'Bukhara'),
        ('ferghana', 'Ferghana'),
        ('jizzakh', 'Jizzakh'),
        ('kashkadarya', 'Kashkadarya'),
        ('khorezm', 'Khorezm'),
        ('namangan', 'Namangan'),
        ('navoiy', 'Navoiy'),
        ('samarkand', 'Samarkand'),
        ('surkhandarya', 'Surkhandarya'),
        ('syrdarya', 'Syrdarya'),
        ('tashkent', 'Tashkent'),
        ('tashkent_city', 'Tashkent City'),
    ], 'Branch Address', required=True)
    code = fields.Char('Branch Code', required=True, size=7)
    phone = fields.Char('Phone')
    email = fields.Char('Email')