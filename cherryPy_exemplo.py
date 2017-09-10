# -*- coding:utf-8 -*-
'''
Web com operações CRUD
'''
# CherryPy
import cherrypy

# CherryTemplate
import cherrytemplate

# SQLAlchemy
import sqlalchemy as sql

db = sql.create_engine('sqlite:///restaura')


class Root(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'


cherrypy.quickstart(Root())
