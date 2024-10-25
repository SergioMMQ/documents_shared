# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import models, fields, exceptions

class Review(models.Model):
    _name = 'documents.review'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Revisiones para los documentos'
    
    name = fields.Many2one("documents.shared", string='Documento')
    review = fields.Char(string="Número de revisión")
    file = fields.Binary(string='Archivo')
    user_id = fields.Many2one("res.users", string="Creador de la revisión")
    state_review = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En proceso'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado'),
    ], string="Estado", default="draft")
    
    folder_id = fields.Many2one('documents.file', string='Carpeta')
    edit_groups_id = fields.Many2many('res.groups', string='Grupos de edición', related='folder_id.edit_groups_id')

    edit_groups_id = fields.Many2many(
        'res.groups',
        'documents_review_edit_relE',  # Cambia este nombre para que sea único
        'review_id', 
        'group_id',
        string='Grupos de edición', 
        related='folder_id.edit_groups_id'
    )