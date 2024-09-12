from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = "property"
    _description = "Property"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, default="New", size=12)
    description = fields.Text(tracking=1)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=1)
    expected_selling_date = fields.Date()
    is_late = fields.Boolean()
    expected_price = fields.Float()
    selling_price = fields.Float()
    Diff = fields.Float(compute="_compute_Diff", readonly=False)  # , store=1
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        default="north",
    )

    active = fields.Boolean(default="True")

    owner_id = fields.Many2one("owner")

    owner_phone = fields.Char(related="owner_id.phone", readonly=False)
    owner_address = fields.Char(related="owner_id.address", readonly=False)

    tag_ids = fields.Many2many("tag")

    line_ids = fields.One2many("property.line", "property_id")

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("sold", "Sold"),
            ("closed", "Closed"),
        ],
        default="draft",
    )

    _sql_constraints = [("unique_name", "unique(name)", "This name already exists!")]

    @api.depends("expected_price", "selling_price", "owner_id.phone")
    def _compute_Diff(self):
        for rec in self:
            print(rec)
            print("inside compute_diff method")
            rec.Diff = rec.expected_price - rec.selling_price

    # views fields only
    @api.onchange("expected_price")
    def _onchange_expected_price(self):
        for rec in self:
            print(rec)
            print("inside onchange_expected_price method")
            return {
                "warning": {
                    "title": "warning",
                    "message": "negative value",
                    "type": "notification",
                }
            }

    # self >>> for one rec or record set ?? though we use for loop to determine one record
    @api.constrains("bedrooms")
    def _check_bedrooms_greater_than_zero(self):
        for rec in self:
            if rec.bedrooms <= False:
                raise ValidationError(
                    "The number of bedrooms must be greater than zero."
                )

    # CRUD operation  >> Create, read, update, delete
    # overriding
    @api.model_create_multi
    def _create(self, data_list):
        res = super(Property, self)._create(data_list)
        # logic
        print("inside create method")

        return res

    # read
    @api.model
    def _search(
        self, domain, offset=False, limit=None, order=None, access_rights_uid=None
    ):
        res = super(Property, self)._search(
            domain, offset=False, limit=None, order=None, access_rights_uid=None
        )
        # logic
        print("inside search method")
        return res

    # update
    def write(self, vals):
        res = super(Property, self).write(vals)
        # logic
        print("inside write method")
        return res

    def action_draft(self):
        for rec in self:
            print("inside draft action")
            rec.state = "draft"

    # ==    rec.write({'state': 'draft' })

    def action_pending(self):
        for rec in self:
            print("inside pending action")
            rec.state = "pending"

    def action_sold(self):
        for rec in self:
            print("inside sold action")
            rec.state = "sold"

    # server action example
    def action_closed(self):
        for rec in self:
            rec.state = "closed"

    def check_expected_selling_date(self):

        property_ids = self.search([])
        for rec in property_ids:
            if (
                rec.expected_selling_date
                and rec.expected_selling_date < fields.date.today()
            ):
                rec.is_late = True
            print(rec)

        print("inside check_expected_selling_date")

    class PropertyLine(models.Model):
        _name = "property.line"

        property_id = fields.Many2one("property")
        area = fields.Float()
        description = fields.Char()
