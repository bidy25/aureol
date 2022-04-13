# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    stat = fields.Char('STAT')
    nif = fields.Char('NIF')
    rcs = fields.Char('RCS')
