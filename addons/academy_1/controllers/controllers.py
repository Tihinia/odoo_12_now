# -*- coding: utf-8 -*-
from odoo import http

# class Academy1(http.Controller):
    # @http.route('/academy_1/academy_1/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    # @http.route('/academy_1/academy_1/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('academy_1.listing', {
    #         'root': '/academy_1/academy_1',
    #         'objects': http.request.env['academy_1.academy_1'].search([]),
    #     })

#     @http.route('/academy_1/academy_1/objects/<model("academy_1.academy_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_1.object', {
#             'object': obj
#         })