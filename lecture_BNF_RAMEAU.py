#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys, os



#//////////////////// Conversion vers UTF 8 //////////////////////////////////
#//////////////////// lancer ces commandes dans le terminal///////////////////

#iconv -f macintosh -t utf-8 RAMEAU-Groupes_ethniques-2.txt > RAMEAU_utf-8.txt
#iconv -f macintosh -t utf-8 BNF_traditions_field.txt > BNF_utf-8.txt



#//////////////////// on ouvre le fichier BNF , lecture ligne par ligne
file1 =open('BNF_utf-8.txt','r')
read1= file1.read()

#/////////////////// on ouvre le fichier RAMEAU , lecture ligne par ligne
file2 = open('RAMEAU_utf-8.txt','r')
read2 = file2.read()



#/////////////////// MESURE LEVENSTEIN ////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////

def levenshtein(mot1,mot2):
	ligne_i = [ k for k in range(len(mot1)+1) ]
	for i in range(1, len(mot2) + 1):
		ligne_prec = ligne_i
		ligne_i = [i]*(len(mot1)+1)
		for k in range(1,len(ligne_i)):	
			cout = int(mot1[k-1] != mot2[i-1])	
			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)	
	return ligne_i[len(mot1)]
	



#print (levenshtein(termeBNF3, termeRM2))

#/////////////////// création de deux nouveaux fichiers en écrtiture
#////////////////// création d'un fichier pour aligner les termes des deux fichiers

nFichierBNF = open('newBNF_utf-8.txt','x+')
nFichierRM = open('newRAMEAU_utf-8.txt','x+')

#nAlignement = open('AlignementBNF_RAMEAU.txt','x+')


#//////////////// on parcour le fichier BNF , on récupère dans tout les lignes que la partie aprés le dernier $ 
#/////////////// on écrit ces lignes là dans le nouveau fichier BNF
res1 = re.findall(r"(\d{8})\n\d{3}\s+\$.*\$[a-z](.*)",read1)
if res1:
	for ligne in res1:	
		#print(ligne,'\n')
		nFichierBNF.write(str(ligne)+'\n')

res2 = re.findall(r"(\d{8})\s+\$a(.+)\$",read2)
if res2:
	for line in res2:
		#print(line,'\n')
		nFichierRM.write(str(line)+'\n')

nFichierBNF.close()
nFichierRM.close()

#/////////////// on collecte les termes à mesurer //////////////////////////

mots1 = open('newBNF_utf-8.txt','r')
read_mots1= mots1.read()

mots2 = open('newRAMEAU_utf-8.txt','r')
read_mots2= mots2.read()

res_mots1 = re.findall(r".*'(.*)'\)",read_mots1)
if res_mots1:
	for ligne1 in res_mots1:
		mot1 = ligne1
		res_mots2 = re.findall(r".*'(.*)'\)",read_mots2)
		if res_mots2:
			for ligne2 in res_mots2:
				mot2 = ligne2
				if levenshtein(mot1, mot2) < 2:
					print(mot1,'    <>    ',mot2,' : ',+levenshtein(mot1,mot2))

