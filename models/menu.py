# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Customers'), False, URL('default', 'customers'), []),
    (T('Schedule'), False, URL('default', 'schedule'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if auth.requires_membership('administrator')==True:
    _app = request.application
    response.menu += [
        (T('Admin'), False, URL('default', 'administrator'), [])
    ]
