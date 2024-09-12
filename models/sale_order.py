from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    property_id = fields.Many2one("property")
    car_id = fields.Many2one("cars")

    car_chassis_number = fields.Char(related="car_id.chassis_number")
    car_color = fields.Char(related="car_id.color")
    car_country = fields.Char(related="car_id.country")

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("inside action_confirm method")
        return res


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    car_id = fields.Many2one("cars")

    car_chassis_number = fields.Char(related="car_id.chassis_number")
    car_color = fields.Char(related="car_id.color")
    car_country = fields.Char(related="car_id.country")

    # car_field = fields.Char(related='car_id.name', string= 'Car')

    # car_field = fields.Char(related='car_id.name')


# class Product(models.Model):
#     _inherit = 'product'


# car_field = fields.Char(related='car_id.name')
