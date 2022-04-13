# -*- coding: utf-8 -*-
{
    'name': "KS PARTNER FISC",
    'summary': """
        Specific fields for partner by KASIA
        """,
    'description': """
       Specific fields for partner by KASIA
    """,
    'author': "KASIA SARL",
    'website': "http://www.kasia.mg",
    'category': 'Human Resource Management',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_company_inherit_views.xml',
        'views/res_partner_inherit_views.xml',
    ],
    'application': False,
    'installable': True,
}
