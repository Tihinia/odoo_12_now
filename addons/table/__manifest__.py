# -*- coding: utf-8 -*-
{
    'name': "Табель рабочего времени",

    'summary': """ Табелирование рабочего времени""",

    'description': """ Создание и загрузка табелей времени рабочих и ИТР. 
    Сравнение предоставленных табелей с выгрузкой из СКУД. 
    Просмотр и архивация информации из СКУД""",

    'author': "Тихиня Владимир Владимирович",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/index_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images':[],
    'external_dependencies': {
        'python': [
            'xlrd',
            'xlwt',
            'openpyxl',
        ],
    },
    'license':'AGPL-3',
    'installable':True,
    'application':False,
    'auto_install':False,
}