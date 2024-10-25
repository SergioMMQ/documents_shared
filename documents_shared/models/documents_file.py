# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import models, fields

class File(models.Model):
    _name = 'documents.file'
    _description = 'Folders para gestionar los documentos'

    name = fields.Char(string='Nombre', required=True)
    parent_file = fields.Many2one('documents.file', string='Carpeta padre', ondelete='cascade')
    child_file = fields.One2many('documents.file', 'parent_file', string='Carpetas hijas', readonly=True)
    documents = fields.One2many('documents.shared', 'folder_id', string='Documentos')
    write_date = fields.Datetime(string='Fecha de actualización', readonly=True)
    
    edit_groups_id = fields.Many2many(
        'res.groups',
        'documents_folder_edit_relE',  # Cambia este nombre si ya existe otra tabla con este nombre
        'folder_id', 
        'group_id',
        string='Grupos que pueden editar'
    )