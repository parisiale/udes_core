# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'UDES Core Functionality',
    'version': '11.0',
    'summary': 'Inventory, Logistics, Warehousing',
    'description': "Holds core functionality for UDES Modules",
    'depends': ['stock'],
    'category': 'Warehouse',
    'sequence': 11,
    'demo': [
    ],
    'data': [
        'data/stock_config.xml',
        'views/product_template.xml',
        'views/stock_location.xml',
        'views/stock_picking.xml',
    ],
    'qweb': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
