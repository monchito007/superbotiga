# -*- coding: utf-8 -*- 
#! usr/bin/python

import os

here = os.path.dirname(os.path.abspath(__file__))

class dades_productes(object):
    
    def __init__(self):
        pass
        
    def getProductes(self):
        
        # productes = open("/home/usuari/env/simpleshop/simpleshop/database/productes.txt","r")
	
        productes = open(os.path.join(here, '../database/productes.txt'),'r')
	
        #Creem una llista per emmagatzemar cadascun dels productes.
        llista_id_productes = [] #Llista ID's
        llista_nom_productes = [] #Llista noms
        llista_stock_productes = [] #Llista stock
        llista_preu_productes = [] #Llista preus
        llista_producte = [] 
	
        #Creem un diccionari per emmagatzemar les dades de cada producte.
        dict_productes = {}
	
        #Obrim l'arxiu de productes per guardar-los en una llista.
        for producte in productes.readlines():
            llista_producte = producte.split("\t")
            llista_id_productes.append(llista_producte[0])
            llista_nom_productes.append(llista_producte[1])
            llista_stock_productes.append(llista_producte[2])
            llista_preu_productes.append(llista_producte[3])
		
        #Tanquem l'arxiu de productes.	
        productes.close()
            
        #Guardem les dades dels productes en un diccionari.
        
        #Crearem un diccionari de diccionaris per emmagatzemar les dades del productes.
        for nom_producte in llista_nom_productes:
            dict_productes[nom_producte] = {}
        
        #Contador per saber en quin producte ens trobem.
        cont = 0
        
        #Omplim el diccionari de diccionaris amb les dades.
        for producte in llista_nom_productes:
            dict_productes[producte]['id'] = int(llista_id_productes[cont])
            #dict_productes[producte]['nom'] = llista_nom_productes[cont]
            dict_productes[producte]['stock'] = int(llista_stock_productes[cont])
            dict_productes[producte]['preu'] = float(llista_preu_productes[cont])
            cont = cont + 1
            
        return { "dades_productes":dict_productes }
        
        
#productes = dades_productes()

#dic_productes = productes.getProductes()

#print dic_productes['dades_productes']['pomes']['preu']


