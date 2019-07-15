from odoo import models, fields


class PaymentMethod(models.Model):
    _name = 'res.partner.use.method'

    name = fields.Char('Name')
    code  = fields.Char('Code')
    description = fields.Char('description') 


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_uso = fields.Many2one('res.partner.use.method', string="uso")