# -*- coding: utf-8 -*- 
#! usr/bin/python

import os

here = os.path.dirname(os.path.abspath(__file__))

class dades_productes(object):
    
    def __init__(self):
        pass
        #self.arxiu_productes = open(os.path.join(here, 'database/productes.txt'),'a+')
        #return None
    
    def getProductes(self):
        
        #arxiu_productes = open("/home/usuari/env/simpleshop/simpleshop/database/productes.txt","r")
        arxiu_productes = open(os.path.join(here, 'database/productes.txt'),'r')

        #Creem una llista per emmagatzemar cadascun dels productes.
        llista_id_productes = [] #Llista ID's
        llista_nom_productes = [] #Llista noms
        llista_stock_productes = [] #Llista stock
        llista_preu_productes = [] #Llista preus
        llista_producte = [] 
    
        #Creem un diccionari per emmagatzemar les dades de cada producte.
        dict_productes = {}
    
        #Obrim l'arxiu de productes per guardar-los en una llista.
        for producte in arxiu_productes.readlines():
            llista_producte = producte.split("\t")
            llista_id_productes.append(llista_producte[0])
            llista_nom_productes.append(llista_producte[1])
            llista_stock_productes.append(llista_producte[2])
            llista_preu_productes.append(llista_producte[3])
        
        #Tanquem l'arxiu de productes.  
        arxiu_productes.close()
            
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
            
        return dict_productes
        
    def obtenir_preu_comanda(self,dict_productes):
        
        arxiu_productes = open(os.path.join(here, 'database/productes.txt'),'r')
        
        #Creem una llista per emmagatzemar cadascun dels productes.
        llista_preus_productes = [] #Llista stock

        #Obrim l'arxiu de productes per guardar-los en una llista.
        for producte in arxiu_productes:
            llista_producte = producte.split("\t")
            llista_preus_productes.append(float(llista_producte[3]))
            
        #Tanquem l'arxiu de productes.  
        arxiu_productes.close()
        
        preu_total = 0
        
        preu_total += dict_productes['pomes']*llista_preus_productes[0]
        preu_total += dict_productes['peres']*llista_preus_productes[1]
        preu_total += dict_productes['platans']*llista_preus_productes[2]
        preu_total += dict_productes['taronges']*llista_preus_productes[3]
        preu_total += dict_productes['llimones']*llista_preus_productes[4]
        preu_total += dict_productes['pastanagues']*llista_preus_productes[5]
        preu_total += dict_productes['raim']*llista_preus_productes[6]
        
        return preu_total
        
    

#dict_comanda = { "id_client":id_client, "pomes":num_pomes, "peres":num_peres, "platans":num_platans, "taronges":num_taronges, "llimones":num_llimones, "pastanagues":num_pastanagues, "raim":num_raim }

#dict_comanda = {'peres': 10, 'platans': 0, 'llimones': 0, 'pomes': 0, 'raim': 0, 'taronges': 0, 'id_client': 20565777, 'pastanagues': 0}     

#classe_productes = dades_productes()

#preu = classe_productes.obtenir_preu_comanda(dict_comanda)

#print preu

#print classe_productes

#print preu_comanda

#dic_productes = productes.getProductes()

#print dic_productes['dades_productes']['pomes']['preu']


