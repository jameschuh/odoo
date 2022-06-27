# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property description"
    _order = "name"

    name = fields.Char(string='Estate Name', required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    date_availability = fields.Date(string="Available Date")
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bed Rooms",default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Have Garage")
    garden = fields.Boolean(string="Have Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation= fields.Selection([('north','North'),('south','South'),("east","East"),("west","West")],string="Garden Orientation")
    active = fields.Boolean(string="Is Active",default=True)
    state = fields.Selection([('New','New'),('Offer Received','Offer Received'),('Offer Accepted','Offer Accepted'),('Sold','Sold'),('Canceled','Canceled')],string="Statu",default="New")

    # type id
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    # tag
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    # buyer
    buyer_id = fields.Many2one("res.partner", string="Buyer",index=True)

    # salesperson
    partner_id = fields.Many2one("res.users", string="Salesperson", index=True, tracking=True, default=lambda self: self.env.user)

    # offer_ids
    offer_ids = fields.One2many('estate.property.offer', 'partner_id', string='Offer')

    #_sql_constraints = [
    #    ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    #]
