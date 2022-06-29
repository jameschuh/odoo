# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


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
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offer')

    # computed field area
    total_area = fields.Float(compute="_compute_total_area", string="Total Area")

    # conputed field area
    #best_price = fields.Float(string="Best Offer")
    best_price = fields.Float(compute="_compute_best_offer_price", string="Best Offer", default=0)

    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.garden_area + rec.living_area

    @api.depends("offer_ids.price")
    def _compute_best_offer_price(self):
        for rec in self:
            if rec.offer_ids:
                for offer in rec.offer_ids:
                    if rec.best_price:
                        rec.best_price = offer.price if rec.best_price < offer.price else rec.best_price
            else:
                rec.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ''
