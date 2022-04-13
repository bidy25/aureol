# -*- coding: utf-8 -*-

from odoo import models, fields


class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    main_activity = fields.Char('Main activity')
    stat = fields.Char('STAT')
    nif = fields.Char('NIF')
    member_code = fields.Char('Member code')
    cnaps = fields.Char('N° CNaPS Employer')
    rcs = fields.Char('RCS')