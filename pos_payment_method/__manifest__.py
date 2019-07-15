# -*- coding: utf-8 -*-
{
    'name': 'Pos Payment Method',
    'version': '11.0.1.0.0',
    'category': 'point_of_sale',
    'summary': 'Point of Sale',
    'author': 'Vperfectcs',
    'license': '',
    'website': 'http://www.vperfectcs.com/',
    'depends': ['point_of_sale', 'contacts'],
    "data": [
        'views/templates.xml',
        #'views/view_payment.xml',
       # 'views/vista_uso.xml',
    ],
    'qweb': [
        'static/src/xml/pos_payment_method.xml',
    ],
    'sequence': 0,
    'installable': True,
    'auto_install': False,
}
