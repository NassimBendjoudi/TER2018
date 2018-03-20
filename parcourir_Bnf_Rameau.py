#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys



#//////////////////// on ouvre le fichier BNF , lecture ligne par ligne
file1 =open('BNF_utf-8.txt','r')
read1= file1.read()



#/////////////////// on ouvre le fichier RAMEAU , lecture ligne par ligne
file2 = open('RAMEAU_utf-8.txt','r')
read2 = file2.read()




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






""" #temchi
for x in read1:
	identifiant = re.search(r"(\d{8})",x)

	termes1 = re.search(r"\d{3}\s+\$.*\$[a-z](.*)",x)

	#identifiants = re.search(r"(\d{8})",ligne)
	#if identifiants:

	if termes1:
		termeBNF = termes1.group(1)
		#print(termeBNF)

	if identifiant :
		identifiant1 = identifiant.group(1)

print(termeBNF,":",identifiant1)
		

	
"""
		#nFichierBNF.write(identifiant1 +" : "+termeBNF3)




	
#//////////////// on parcour le fichier RAMEAU , on récupère dans tout les lignes que la partie aprés le $a , on remplace les $g  par des "-"
#/////////////// on écrit ces lignes là dans le nouveau fichier RAMEAU


res2 = re.findall(r"(\d{8})\s+\$a(.+)\$",read2)
if res2:
	for ligne in res2:	
		#print(ligne,'\n')
		
		nFichierRM.write(str(ligne)+'\n')








"""
for y in read2 :
	lignes = re.search(r"(\d{8})\s+\$a(.+)\$", y)

	if lignes:

		identifiant2 = lignes.group(1)

	
		termeRM=lignes.group(2)
		
		
		print(identifiant+termeRM)

		nFichierRM.write("\n"+termeRM)
		

		#nAlignement.write("\n"+termeBNF3+"       "+termeRM2)

"""
#def levenshtein(mot1,mot2):
	
#	ligne_i = [ k for k in range(len(mot1)+1) ]

#	for i in range(1, len(mot2) + 1):

#		ligne_prec = ligne_i
		
#		ligne_i = [i]*(len(mot1)+1)

#		for k in range(1,len(ligne_i)):
			
#			cout = int(mot1[k-1] != mot2[i-1])
			
#			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
			
#	return ligne_i[len(mot1)]
	



#print (levenshtein(termeBNF3, termeRM2))



