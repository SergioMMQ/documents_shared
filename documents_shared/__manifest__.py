# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Documentos compartidos',
    'summary': 'Optimiza la organización de documentos y carpetas, facilitando el seguimiento de revisiones y cambios. Esta solución permite una administración eficiente de archivos, asegurando un acceso controlado y un historial claro de modificaciones.',
    'author': 'Sergio Martinez Meneses',
    'company': 'Quetzalcode',
    'maintainer': 'Sergio Martinez Meneses',
    'website': 'https://sergiommq.github.io/portafolio/',
    'category': 'Customer Service',
    'version': '1.0.3',
    'description': """
        Esta solución permite optimizar la organización de documentos y carpetas, mejorando la eficiencia en el seguimiento de revisiones y cambios. Facilita un acceso controlado a los archivos, garantizando la integridad de la información y un historial claro de modificaciones. Además, ofrece herramientas de colaboración que fomentan el trabajo en equipo y aseguran que todos los usuarios estén alineados con los procesos de revisión y aprobación.
    """,
    'depends': ['base', 'base_setup', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_menu.xml',
        'views/documents_shared.xml',
        'views/documents_review.xml',
        'views/documents_file.xml',
        'views/documents_search.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'price': 90,
    'currency': 'USD',
    'support': 'quetzal.mq97@gmail.com',
}
