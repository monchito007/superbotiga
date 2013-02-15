# -*- coding: utf-8 -*- 
#! usr/bin/python
import os
import random
from classe_productes import dades_productes
from classe_comandes import comandes

from pyramid.view import view_config
here = os.path.dirname(os.path.abspath(__file__))


@view_config(route_name='home', renderer='benvinguda.mako')
def my_view(request):
    return {'project':'simpleshop'}
    
@view_config(route_name='productes', renderer='productes.mako')
def llista_prod_view(request):
    productes = dades_productes()
    dic_productes = productes.getProductes()
    return { "dades_productes":dic_productes, "projecte": 'SimpleShop' }
    
@view_config(route_name='llista_productes', renderer='llista_productes.mako')
def productes_view(request):
    productes = dades_productes()
    dic_productes = productes.getProductes()
    return { "dades_productes":dic_productes, "projecte": 'SimpleShop' }

@view_config(route_name='comandes', renderer='form_comandes.mako')
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
	return { "id_comanda":str(id_comanda), "id_client":str(id_client), "pomes":num_pomes, "peres":num_peres, "platans":num_platans, "taronges":num_taronges, "llimones":num_llimones, "pastanagues":num_pastanagues, "raim":num_raim, "preu":preu_comanda }
		
@view_config(route_name='llistat_comandes', renderer='llistat_comandes.mako')
def llistat_comandes_view(request):
    llistat_comandes = comandes()
    dict_comandes = llistat_comandes.llistar_comandes()
    return { "dict_comandes":dict_comandes, "projecte": 'SimpleShop' }
    
    
    
