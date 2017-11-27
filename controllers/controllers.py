# -*- coding: utf-8 -*-
from odoo import http

# class Namche(http.Controller):
#     @http.route('/namche/namche/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/namche/namche/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('namche.listing', {
#             'root': '/namche/namche',
#             'objects': http.request.env['namche.namche'].search([]),
#         })

#     @http.route('/namche/namche/objects/<model("namche.namche"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('namche.object', {
#             'object': obj
#         })