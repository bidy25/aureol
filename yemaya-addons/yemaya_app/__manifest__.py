# -*- coding: utf-8 -*-
{
    'name': "yemaya_app",
    'summary': """ YEMAYA """,
    'description': """ YEMAYA""", 'author': "KASIA SARL",
    'website': "https://kasia.mg",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'accounting_pdf_reports',
        'backend_theme_v14',
        'ks_partner_fisc',
        'om_account_accountant',
        'om_account_asset',
        'om_account_bank_statement_import',
        'om_account_budget',
        'web_responsive',
        'yemaya_base',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
}
