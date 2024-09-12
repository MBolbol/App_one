from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    car_id = fields.Many2one("cars")

    car_chassis_number = fields.Char(related="car_id.chassis_number")
    car_color = fields.Char(related="car_id.color")
    car_country = fields.Char(related="car_id.country")
