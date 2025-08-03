# -*- coding: utf-8 -*-

{
    'name': 'Approvals Override',
    'version': '1.0.0',
    'category' : 'Approvals',
    'sequence' : 10,
    'summary' : 'Modifies Approvals module',
    'description' : """Modifcation module for Approvals""",
    'author' : "Mostafa Yasser",
    'depends' : ['base' , 'approvals' , 'hr'],
    'data' : [
        'security/ir.model.access.csv',
        'views/approvals_inherited_view.xml',
    ],
    'demo' : [],
    'application' : False,
    'installable' : True,
    'auto_install' : False,
    'license' : 'LGPL-3'
}
