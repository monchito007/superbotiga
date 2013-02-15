# -*- coding: utf-8 -*- 

from pyramid.config import Configurator
import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    settings['mako.directories'] = os.path.join(here, 'templates')
    
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('llista_productes', '/llista_productes') #productes = ruta , /botiga=URL
    config.add_route('productes', '/productes') #productes = ruta , /botiga=URL
    config.add_route('comandes', '/comandes') #productes = ruta , /botiga=URL
    config.add_route('llistat_comandes', '/llistat_comandes') #productes = ruta , /botiga=URL
    config.scan()
    return config.make_wsgi_app()
