# -*- coding: utf-8 -*-
from odoo import http

# class Test-shafco(http.Controller):
#     @http.route('/test-shafco/test-shafco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test-shafco/test-shafco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test-shafco.listing', {
#             'root': '/test-shafco/test-shafco',
#             'objects': http.request.env['test-shafco.test-shafco'].search([]),
#         })

#     @http.route('/test-shafco/test-shafco/objects/<model("test-shafco.test-shafco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test-shafco.object', {
#             'object': obj
#         })