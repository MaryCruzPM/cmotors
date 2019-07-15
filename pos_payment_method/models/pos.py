from odoo import models, fields


class PaymentMethod(models.Model):
    _name = 'res.partner.payment.method'

    name = fields.Char('Name')
    code  = fields.Char('Code')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    payment_method_id = fields.Many2one('res.partner.payment.method', string="Way to pay")