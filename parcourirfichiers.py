#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
import re

#/// On va traiter un fichier avec des caractères ASCII et non tous UTF-8 donc on doit procéder à une convertion vers UTF-8 /////


fichier1 = codecs.open('BNF_traditions_field.txt','r','utf-8')

lecture = fichier1.readlines()

listeOrigine = list()

for ligne in lecture:
	#print(ligne)
	expression = re.compile(r"[0-9]{3}\s+.*\$a.*(\$m.*)")
	#mot = re.search("[0-9]{3}\s+\$a(.*)\$m(.*)\$m(.*)$", lecture)
	#filename = splitext(basename(filepath))[0]
	mot = re.search(expression, ligne)
		
	if mot:
		#ethnie = mot.group(1)
		#continent = mot.group(2)
		origine = mot.group(1)
		origine1 = origine.replace('$m','')
		origine2 = origine1.replace('$e',',')
		origine3 = origine2.replace('-','')
		print(origine2)
		#listeOrigine.append(origine2)
		




#143   $aTraditions$mAfrique du Nord$mMaroc
#38563024

