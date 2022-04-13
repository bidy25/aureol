# -*- coding: utf-8 -*-
# from odoo import http


# class YemayaBase(http.Controller):
#     @http.route('/yemaya_base/yemaya_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yemaya_base/yemaya_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yemaya_base.listing', {
#             'root': '/yemaya_base/yemaya_base',
#             'objects': http.request.env['yemaya_base.yemaya_base'].search([]),
#         })

#     @http.route('/yemaya_base/yemaya_base/objects/<model("yemaya_base.yemaya_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yemaya_base.object', {
#             'object': obj
#         })
