# -*- coding: utf-8 -*-
from odoo import http

# class Custom-purchase(http.Controller):
#     @http.route('/custom-purchase/custom-purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-purchase/custom-purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-purchase.listing', {
#             'root': '/custom-purchase/custom-purchase',
#             'objects': http.request.env['custom-purchase.custom-purchase'].search([]),
#         })

#     @http.route('/custom-purchase/custom-purchase/objects/<model("custom-purchase.custom-purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-purchase.object', {
#             'object': obj
#         })