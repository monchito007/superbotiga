# -*- coding: utf-8 -*- 
#! usr/bin/python
from pyramid.httpexceptions import HTTPFound

from pyramid.view import (
    view_config,
    forbidden_view_config,
)
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
)
from .security import comprova_usuari
#
import os
import random
from classe_productes import dades_productes
from classe_comandes import comandes

from pyramid.view import view_config
here = os.path.dirname(os.path.abspath(__file__))


@view_config(route_name='home', renderer='benvinguda.mako')
def my_view(request):
    return {'project':'simpleshop', 'logged_in':authenticated_userid(request)}
    
@view_config(route_name='productes', renderer='productes.mako', permission='clients')
def llista_prod_view(request):
    productes = dades_productes()
    dic_productes = productes.getProductes()
    return { "dades_productes":dic_productes, "projecte": 'SimpleShop', 'logged_in':authenticated_userid(request) }
    
@view_config(route_name='llista_productes', renderer='llista_productes.mako')
def productes_view(request):
    productes = dades_productes()
    dic_productes = productes.getProductes()
    return { "dades_productes":dic_productes, "projecte": 'SimpleShop', 'logged_in':authenticated_userid(request) }

@view_config(route_name='comandes', renderer='form_comandes.mako', permission='clients')
def comandes_view(request):
	if request.method == 'POST':
		
		if request.POST.get('pomes'):
			num_pomes = int(request.POST.get('pomes'))
		else:
			num_pomes = 0
		
		if request.POST.get('peres'):
			num_peres = int(request.POST.get('peres'))
		else:
			num_peres = 0
	
		if request.POST.get('platans'):
			num_platans = int(request.POST.get('platans'))
		else:
			num_platans = 0
			
		if request.POST.get('taronges'):
			num_taronges = int(request.POST.get('taronges'))
		else:
			num_taronges = 0
			
	
		if request.POST.get('llimones'):
			num_llimones = int(request.POST.get('llimones'))
		else:
			num_llimones = 0
			
	
		if request.POST.get('pastanagues'):
			num_pastanagues = int(request.POST.get('pastanagues'))
		else:
			num_pastanagues = 0
			
	
		if request.POST.get('raim'):
			num_raim = int(request.POST.get('raim'))
		else:
			num_raim = 0
        
        #creem un ID aleatori per al client de la comanda.    
        id_client = random.randrange(10000000,99999999)
        
        dict_comanda = { "id_client":id_client, "pomes":num_pomes, "peres":num_peres, "platans":num_platans, "taronges":num_taronges, "llimones":num_llimones, "pastanagues":num_pastanagues, "raim":num_raim }
        
	#print "Tipus de  dades %s" % type(num_pomes)
	
        #Creem un objecte productes per obtenir el preu total de la comanda
        classe_productes = dades_productes()
        #preu_comanda = productes.obtenir_preu(dict_comanda)
	
	print dict_comanda
        
        #Obtenim el preu de la comanda.
        preu_comanda = classe_productes.obtenir_preu_comanda(dict_comanda)
	
	#print "preu_comanda -> %d" % preu_comanda
        
        #Creem un objecte comanda
        obj_comanda = comandes()
        #Afegim la comanda
        obj_comanda.afegir_comanda(dict_comanda, str(preu_comanda))
        
        #Obtenim l'ID de l'ultima comanda
        id_comanda = obj_comanda.obtenir_ultim_id()
	
	#print "Ultim ID -> %d" % id_comanda
        
	#return { "id_comanda":str(id_comanda), "id_client":str(id_client), "pomes":num_pomes, "peres":num_peres, "platans":num_platans, "taronges":num_taronges, "llimones":num_llimones, "pastanagues":num_pastanagues, "raim":num_raim}
	return { "id_comanda":str(id_comanda), "id_client":str(id_client), "pomes":num_pomes, "peres":num_peres, "platans":num_platans, "taronges":num_taronges, "llimones":num_llimones, "pastanagues":num_pastanagues, "raim":num_raim, "preu":preu_comanda, 'logged_in':authenticated_userid(request) }
		
@view_config(route_name='llistat_comandes', renderer='llistat_comandes.mako', permission='master')
def llistat_comandes_view(request):
    llistat_comandes = comandes()
    dict_comandes = llistat_comandes.llistar_comandes()
    return { "dict_comandes":dict_comandes, "projecte": 'SimpleShop', 'logged_in':authenticated_userid(request) }

    
# aquest decorator és per establir la ruta per /login
@view_config( route_name='login', renderer='login.mako')
# aquest altre ens redirigirà aquí quan algú intenti entrar en una web que no té permís
@forbidden_view_config(renderer='login.mako')
def login(request):
    login_url = request.route_url('login')
    # detectem des de quina URL ve el visitant
    referrer = request.url
    # retornem l'usuari a la home page si ha vingut directe al login
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    user = authenticated_userid(request)
    if user:
        lloc = came_from.split("/")
        #message = "Ets %s, i com a tal no pots entrar a %s" % (user,lloc[len(lloc)-1])
	message = "Ets %s, i com a tal no pots entrar a la Superbotiga" % (user)
    else:
        message = "Identifica't per entrar a la Superbotiga"
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if comprova_usuari(login,password):
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        user = authenticated_userid(request), # afegim usuari autenticat si l'hi ha
        )
    

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('home'),
                     headers = headers)
    
