# -*- coding: utf-8 -*-
# from odoo import http


# class YemayaApp(http.Controller):
#     @http.route('/yemaya_app/yemaya_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yemaya_app/yemaya_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yemaya_app.listing', {
#             'root': '/yemaya_app/yemaya_app',
#             'objects': http.request.env['yemaya_app.yemaya_app'].search([]),
#         })

#     @http.route('/yemaya_app/yemaya_app/objects/<model("yemaya_app.yemaya_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yemaya_app.object', {
#             'object': obj
#         })
