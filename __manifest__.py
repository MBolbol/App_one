{
    'name': 'App_one',
    'author': 'Mostafa BOlbol',
    'version': '1.0',
    'summary': 'Centralize your address book',

    'depends': ['base','sale','account','mail'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml'

        ],
    'assets':{
        'web.assets_backend':['/App_one/static/source/CSS/property.css']
    },

    'application': True,
    'license': 'LGPL-3',

}