# -*- coding: utf-8 -*- 

from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .security import groupfinder    
from .models import RootFactory
import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    settings['mako.directories'] = os.path.join(here, 'templates')
    
    # afegit del auth module
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(root_factory='.models.RootFactory', settings=settings)
    #config = Configurator(settings=settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('llista_productes', '/llista_productes') #productes = ruta , /botiga=URL
    config.add_route('productes', '/productes') #productes = ruta , /botiga=URL
    config.add_route('comandes', '/comandes') #productes = ruta , /botiga=URL
    config.add_route('llistat_comandes', '/llistat_comandes') #productes = ruta , /botiga=URL
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
