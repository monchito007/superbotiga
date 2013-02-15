# -*- coding: utf-8 -*- 
#! usr/bin/python

import os

here = os.path.dirname(os.path.abspath(__file__))

class comandes(object):
    
    def __init__(self):
        pass
        
    def afegir_comanda(self,comanda, preu):
        
        dades_comanda = open(os.path.join(here, 'database/comandes.txt'),'a+')
        
        cont=0
        
        for registre_comanda in dades_comanda.readlines():
            cont=cont+1
        
        dades_comanda.write("id:%s" % (cont+1))
        dades_comanda.write("\t")
        dades_comanda.write("id_client:%s" % (comanda['id_client']))
        dades_comanda.write("\t")
        dades_comanda.write("pomes:%s" % (comanda['pomes']))
        dades_comanda.write("\t")
        dades_comanda.write("peres:%s" % (comanda['peres']))
        dades_comanda.write("\t")
        dades_comanda.write("platans:%s" % (comanda['platans']))
        dades_comanda.write("\t")
        dades_comanda.write("taronges:%s" % (comanda['taronges']))
        dades_comanda.write("\t")
        dades_comanda.write("llimones:%s" % (comanda['llimones']))
        dades_comanda.write("\t")
        dades_comanda.write("pastanagues:%s" % (comanda['pastanagues']))
        dades_comanda.write("\t")
        dades_comanda.write("raim:%s" % (comanda['raim']))
	dades_comanda.write("\t")
        dades_comanda.write("preu:%s" % preu)
        dades_comanda.write("\n")
	
	dades_comanda.close()
        
    def llistar_comandes(self):
        
        #Llista per les comandes de l'arxiu
        llista_comandes = []
        
        #Llista per als productes i dades.
        llista_id_comanda = []
        llista_id_client = []
        llista_pomes = []
        llista_peres = []
        llista_platans = []
        llista_taronges = []
        llista_llimones = []
        llista_pastanagues = []
        llista_raim = []
	llista_preus = []
        
        #Diccionari per emmagatzemar les comandes
        dict_comandes = {}
        
        #Llistes per guardar les dades temporalment
        temp_id_comanda = []
        temp_id_client = []
        temp_pomes = []
        temp_peres = []
        temp_platans = []
        temp_taronges = []
        temp_llimones = []
        temp_pastanagues = []
        temp_raim = []
	temp_preu = []
        
        dades_comandes = open(os.path.join(here, 'database/comandes.txt'),'r')
        
        
        
        for comandes in dades_comandes:
            
            print "comanda: %s" % comandes
            
            if comandes!="":
            #if len(comandes)>10:
            
                #Guardar les dades temporalment
                llista_comandes = comandes.split("\t")
                temp_id_comanda = llista_comandes[0].split(":")
                temp_id_client = llista_comandes[1].split(":")
                temp_pomes = llista_comandes[2].split(":")
                temp_peres = llista_comandes[3].split(":")
                temp_platans = llista_comandes[4].split(":")
                temp_taronges = llista_comandes[5].split(":")
                temp_llimones = llista_comandes[6].split(":")
                temp_pastanagues = llista_comandes[7].split(":")
                temp_raim = llista_comandes[8].split(":")
		temp_preu = llista_comandes[9].split(":")
                
                llista_id_comanda.append(int(temp_id_comanda[1])) 
                llista_id_client.append(temp_id_client[1])
                llista_pomes.append(temp_pomes[1])
                llista_peres.append(temp_peres[1]) 
                llista_platans.append(temp_platans[1]) 
                llista_taronges.append(temp_taronges[1])
                llista_llimones.append(temp_llimones[1])
                llista_pastanagues.append(temp_pastanagues[1])
                llista_raim.append(temp_raim[1])
		llista_preus.append(temp_preu[1])
            
        dades_comandes.close()
        
        #Creem un diccionari de diccionaris per guardar les dades de les comandes.
        for id_comanda in llista_id_comanda:
            dict_comandes[id_comanda]={}
            
        cont = 0        
        for id_comanda in dict_comandes.keys():
        #for id_comanda in llista_id_comanda:
            dict_comandes[id_comanda] = { "id":id_comanda, "id_client":llista_id_client[cont], "pomes":llista_pomes[cont], "peres":llista_peres[cont], "platans":llista_platans[cont], "taronges":llista_taronges[cont], "llimones":llista_llimones[cont], "pastanagues":llista_pastanagues[cont], "raim":llista_raim[cont], "preu":llista_preus[cont] }
            cont = cont + 1
        
        return dict_comandes
        
    def obtenir_ultim_id(self):
			
			dades_comanda = open(os.path.join(here, 'database/comandes.txt'),'r')
			
			cont=0
			
			for registre_comanda in dades_comanda.readlines():
				cont=cont+1
				
			dades_comanda.close()
					
			return cont
