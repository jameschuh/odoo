# -*- coding: utf-8 -*-

{
    'name': 'estate',
    'version': '1.0',
    'category': 'Uncategorized',
    'description': 'desc',
    'depends' : ['base'],
    'installable': True,
    'application': True,
    'data': [
            'security/ir.model.access.csv',
            'views/estate_property_views.xml',
            'views/estate_property_type_views.xml',
            'views/estate_property_tag_views.xml',
            'views/estate_property_offer_views.xml',
            'views/estate_menus.xml',
        ]
}
