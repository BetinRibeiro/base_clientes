# -*- coding: utf-8 -*-
db.define_table("distributor",
                    Field('name_distributor', 'string',label=T("name distributor"), notnull=True),
                    Field('whatzapp', 'string',label=T("Whatzapp"), notnull=True),
                    Field('genre', 'string',label=T("genre") ,default=T('feminine')),
                    Field('address', 'string', label=T("address")),
                    Field('date_of_birth', 'date', label=T("date_of_birth"),default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                    Field('marital_status', 'string',label=T("marital_status") ,default=T('married')),
                    Field('note', 'text',label=T("note")),
                    auth.signature,
                    format='%(name_distributor)s')

db.distributor.marital_status.requires = IS_IN_SET([T('not married'), T('dating'), T('married')])
db.distributor.genre.requires = IS_IN_SET([T('male'), T('feminine')])

db.define_table("client",
                    Field("distributor", 'reference distributor', label=T('distributor'),writable=False, readable=True),
                    Field('name_client', 'string',label=T("Name Client"), notnull=True),
                    Field('whatzapp', 'string',label=T("Whatzapp"), notnull=True),
                    Field('genre', 'string',label=T("genre") ,default=T('feminine')),
                    Field('address', 'string', label=T("address")),
                    Field('date_of_birth', 'date', label=T("date_of_birth"),default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                    Field('marital_status', 'string',label=T("marital_status") ,default=T('married'), notnull=True),
                    Field('note', 'text',label=T("note")),
                    format='%(name_client)s')

db.client.marital_status.requires = IS_IN_SET([T('not married'), T('dating'), T('married')])
db.client.genre.requires = IS_IN_SET([T('male'), T('feminine')])

db.define_table("work_activity",
                         Field("client", 'reference client', label=T('client'),notnull=True ,writable=False, readable=True),
                         Field("description", 'string',label=T('Description'),notnull=True),
                         Field('activity_date', 'date', label=T("Activity Date"),default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                         Field('next_date', 'date', label=T("Next Date"),default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                         Field("value_activity", 'double',label=T("Value"), default=0.00 , notnull=True),
                         Field("reschedule", 'boolean',label=T("Reschedule") ),
                         Field("note", 'text', label=T('Note'),notnull=True),
                         auth.signature)

db.work_activity.description.requires = IS_IN_SET([T('Sale'), T('Sale Schedule'),T('Product Presentation'), T('Business Presentation'),T('Invite to Event')])
