# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import datetime


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer description"
    _order = "price"
    
    price = fields.Float(string='Price')
    status = fields.Selection([('Accepted','Accepted'),('Refused','Refused')], string='Status')
    partner_id = fields.Many2one('res.partner', required=True, string='Partner')
        

    property_id = fields.Many2one('estate.property', required=True, string='Property')

    # inverse
    validity = fields.Integer('Validity(days)', default=7)
    date_deadline = fields.Date('Deadline', compute="_compute_deadline", inverse="_inverse_validity_from_deadline")


    # compute field
    @api.depends("validity","create_date")
    def _compute_deadline(self):
        for rec in self:
            if rec.validity:
                d = datetime.timedelta(days=rec.validity)
                if rec.create_date:
                    rec.date_deadline = rec.create_date + d

    def _inverse_validity_from_deadline(self):
        for rec in self:
            if rec.date_deadline and rec.create_date:
                rec.validity = (rec.date_deadline - rec.create_date.date()).days

