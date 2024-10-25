# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import models, fields

class DocumentosShared(models.Model):
    _name = 'documents.shared'
    _description = 'Documentos Compartidos'
    
    name = fields.Char(string="Nombre", required=True)
    author_id = fields.Many2one('res.users', string='Autor', default=lambda self: self.env.user)
    type = fields.Selection([
    ('file', 'Archivo'),
    ('url', 'Enlace'),
    ('image', 'Imagen'),
    ('video', 'Video'),
    ('audio', 'Audio'),
    ], string='Tipo', required=True, default='file')
    type_file = fields.Binary(string='Archivo', compute='_compute_last_revision_file', store=True)
    type_url = fields.Char(string='Enlace')
    type_image = fields.Binary(string='Imagen')
    type_video = fields.Binary(string='Video')
    type_audio = fields.Binary(string='Audio')
    
    date = fields.Datetime(string='Fecha de creación', default=fields.Datetime.now)
    
    files = fields.One2many("documents.review", "name", string="Revisiones")
    folder_id = fields.Many2one('documents.file', string='Carpeta')
    
    