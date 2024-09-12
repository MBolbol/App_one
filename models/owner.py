from odoo import models, fields


class Owner(models.Model):
    _name = "owner"

    name = fields.Char(required=True)
    phone = fields.Char(size=11)
    address = fields.Char()
