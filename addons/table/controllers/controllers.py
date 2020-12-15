# -*- coding: utf-8 -*-
from odoo import http

# class Table(http.Controller):
#     @http.route('/table/table/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/table/table/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('table.listing', {
#             'root': '/table/table',
#             'objects': http.request.env['table.table'].search([]),
#         })

#     @http.route('/table/table/objects/<model("table.table"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('table.object', {
#             'object': obj
#         })