from odoo import models, fields


class Tag(models.Model):
    _name = 'tag'

    name = fields.Char(required=True, default='new', size=12)

