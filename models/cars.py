from odoo import models, fields


class Cars(models.Model):
    _name = "cars"
    _description = "Cars Record"
    _inherit = ("mail.thread", "mail.activity.mixin")

    name = fields.Char(required=True)
    chassis_number = fields.Char(size=17)
    code = fields.Char()
    description = fields.Text()
    color = fields.Char()
    model_year = fields.Date()
    country = fields.Char()
    active = fields.Boolean(default="True")

    # class CarLine(models.Model):
    #     _name = 'car.line'

    #     car_id = fields.Many2one('cars')
