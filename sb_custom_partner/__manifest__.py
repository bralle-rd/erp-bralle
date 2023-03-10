# -*- coding: utf-8 -*-
{
    'name': "sb_custom_partner",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Smart-bussiness [josueflores.05@gmail.com]",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'l10n_mx_edi_40', 'l10n_mx_edi', 'l10n_mx', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        # 'views/sale_order.xml',
        'views/account_move.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
