# -*- coding: utf-8 -*-
# Copyright 2018 Randall Castro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, api


class PartnerSequence(models.Model):
    _inherit = 'res.partner'

    partner_sequence_id = fields.Char('sequence', readonly='True')

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('res.partner') or '/'
        vals['partner_sequence_id'] = seq
        return super(PartnerSequence, self).create(vals)
