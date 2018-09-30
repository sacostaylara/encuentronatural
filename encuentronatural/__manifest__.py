# -*- coding: utf-8 -*-
{
    'name': "Encuentro Natural",

    'summary': "Modulo para Encuentro Natural",

    'description': "Modulo para Encuentro Natural",

    'author': "Santiago Acosta y Lara",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'stock', 'mrp', 'point_of_sale', 'purchase', 'account_invoicing', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/lot_reports.xml',
        'reports/lot_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
