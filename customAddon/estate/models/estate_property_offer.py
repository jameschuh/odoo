# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer description"
    _order = "price"

    price = fields.Float(string='Price')
    status = fields.Selection([('Accepted','Accepted'),('Refused','Refused')], string='Status')
    partner_id = fields.Many2one('res.partner', required=True, string='Partner')
    property_id = fields.Many2one('estate.property', required=True, string='Property')

    #_sql_constraints = [
    #    ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    #]
