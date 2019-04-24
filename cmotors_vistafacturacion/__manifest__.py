# -*- coding: utf-8 -*-
{
    'name': "Apuntes contables en facturacion",
    'description': """
        Agregar la opcion de apuntes contables en facturacion para todos los usuarios
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'account_invoicing',
                'account',
                # 'pos_invoice',
                # 'factura_smart',
                # 'website_delivery_ups',
                ],
    'data': [
        'views/facturacion_apuntescon.xml',

        ],
    'installable':True,
    'auto_install':False,
}
