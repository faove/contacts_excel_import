{
    'name': 'Importar contactos desde Excel',
    'version': '18.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Permite importar contactos desde archivos Excel',
    'author': 'Francisco Alvarez',
    'depends': ['contacts'],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    'data': [
        'views/res_partner_views.xml',
        'views/contact_excel_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
