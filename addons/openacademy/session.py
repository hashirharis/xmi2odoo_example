# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class session(models.Model):
    """"""

    _name = 'openacademy.session'
    _description = 'session'

    name = fields.Char(
        string='Name',
        required=True
        )
    start_date = fields.Date(
        string='Start Date'
        )
    duration = fields.Float(
        string='Durtion',
        digits='(6, 2)',
        required=True
        )
    seats = fields.Integer(
        string='Number of Seats',
        required=True
        )
    instructor_id = fields.Many2one(
        'res.partner',
        string='Instructor'
        )
    course_id = fields.Many2one(
        'openacademy.course',
        ondelete='cascade',
        string='course_id',
        required=True
        )

    _constraints = [
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
