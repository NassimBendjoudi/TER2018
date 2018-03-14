#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
import re, sys



#//////////////////// on ouvre le fichier BNF , lecture ligne par ligne
file1 = codecs.open('BNF_utf-8.txt','r','utf-8')
read1= file1.readlines()



#/////////////////// on ouvre le fichier RAMEAU , lecture ligne par ligne
file2 = codecs.open('RAMEAU_utf-8.txt','r')
read2 = file2.readlines()




#/////////////////// création de deux nouveaux fichiers en écrtiture
#////////////////// création d'un fichier pour aligner les termes des deux fichiers
nFichierBNF = open('newBNF_utf-8.txt','x+')
nFichierRM = open('newRAMEAU_utf-8.txt','x+')
nAlignement = open('AlignementBNF_RAMEAU.txt','x+')


#//////////////// on parcour le fichier BNF , on récupère dans tout les lignes que la partie aprés le $m , on remplace les $e et $i par des "-"
#/////////////// on écrit ces lignes là dans le nouveau fichier BNF

for x in read1:
	termes = re.search(r"\d{3}\s+\$a.*\$m(.*)",x)
	#identifiants = re.search(r"(\d{8})",ligne)
	#if identifiants:
	if termes:	

		termeBNF = termes.group(1) 
		termeBNF2 = termeBNF.replace("$e"," ")
		termeBNF3 = termeBNF2.replace("$i"," ")
		print(termeBNF3)

		nFichierBNF.write("\n"+termeBNF3)
	





	
#//////////////// on parcour le fichier RAMEAU , on récupère dans tout les lignes que la partie aprés le $a , on remplace les $g  par des "-"
#/////////////// on écrit ces lignes là dans le nouveau fichier RAMEAU


for y in read2 :
	lignes = re.search(r"(\d{8})\s+\$a(.+)", y)

	if lignes:

		identifiant = lignes.group(1)

	
		termeRM=lignes.group(2)
		termeRM2=termeRM.replace("$g"," ")
		
		print(termeRM2)

		nFichierRM.write("\n"+termeRM2)
		

		nAlignement.write("\n"+termeBNF3+"       "+termeRM2)


def levenshtein(mot1,mot2):
	
	ligne_i = [ k for k in range(len(mot1)+1) ]

	for i in range(1, len(mot2) + 1):

		ligne_prec = ligne_i
		
		ligne_i = [i]*(len(mot1)+1)

		for k in range(1,len(ligne_i)):
			
			cout = int(mot1[k-1] != mot2[i-1])
			
			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
			
	return ligne_i[len(mot1)]
	



print (levenshtein(termeBNF3, termeRM2))



