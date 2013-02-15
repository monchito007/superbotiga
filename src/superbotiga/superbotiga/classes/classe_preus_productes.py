# -*- coding: utf-8 -*- 
#! usr/bin/python

import os

here = os.path.dirname(os.path.abspath(__file__))

class calcul_comandes(object):
	
	def __init__(self):
		self.preu_total=0
		pass
		
	def obtenir_preu_comanda(self, dict_productes):
		arxiu_productes = open(os.path.join(here, 'database/productes.txt'),'r')
		
		#Creem una llista per emmagatzemar cadascun dels productes.
		llista_stock_productes = [] #Llista stock
        
		#Obrim l'arxiu de productes per guardar-los en una llista.
		for producte in arxiu_productes:
			llista_producte = producte.split("\t")
			llista_stock_productes.append(llista_producte[2])
            
		#Tanquem l'arxiu de productes.	
		arxiu_productes.close()
        
		#preu_total = 0
        
		self.preu_total += dict_productes['pomes']*llista_stock_productes[0]
		self.preu_total += dict_productes['peres']*llista_stock_productes[1]
		self.preu_total += dict_productes['platans']*llista_stock_productes[2]
		self.preu_total += dict_productes['taronges']*llista_stock_productes[3]
		self.preu_total += dict_productes['llimones']*llista_stock_productes[4]
		self.preu_total += dict_productes['pastanagues']*llista_stock_productes[5]
		self.preu_total += dict_productes['raim']*llista_stock_productes[6]
        
        print self.preu_total
