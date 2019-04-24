# -*- coding: utf-8 -*-
{
    'name': "lista inventario",

    'summary': """
        Reporte de listado de inventario
        """,

    'description': """
        Listado de inventario
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock','stock_account',],

    # always loaded
    'data': [
        
        'views/listado_inventario.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}