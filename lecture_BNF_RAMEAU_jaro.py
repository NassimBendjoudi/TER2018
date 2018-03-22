#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
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

#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#///////////////////    MESURE JARO    ////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////

def jaro(mot1, mot2): #s et t étant les chaines de caractère à aligner
    mot1_len = len(mot1) #s_len est le nombre de caractères dans s
    mot2_len = len(mot2) #t_len est le nombre de caractères dans t
 
    if mot1_len == 0 and mot2_len == 0: # si il n y a pas de lettres dans les deux mots, alors retourner la valeur 1 comme distance JARO
        return 1
 
    match_distance = (max(mot1_len, mot2_len) // 2) - 1 # on calcul la moitié de la distance du max des longueurs de s ou t et on soustrait cette valeur à 1
    
    #print('\n','Match_distance :',match_distance) #Console 
    
    mot1_matches = [False] * mot1_len 
    mot2_matches = [False] * mot2_len
 
    matches = 0
    transpositions = 0
 
    for i in range(mot1_len): #on parcours s
        start = max(0, i-match_distance) #start est le max entre 0 et la valeur de i-match_distance
        end = min(i+match_distance+1, mot2_len) #end est le min entre i+match_distance et la longueur de t
 
        for j in range(start, end): #
            if mot2_matches[j]:
                continue
            if mot1[i] != mot2[j]:
                continue
            mot1_matches[i] = True
            mot2_matches[j] = True
            matches += 1
            break
 
    if matches == 0:
        return 0
    #print ('Matches :',matches) #Console
    k = 0
    for i in range(mot1_len):
        if not mot1_matches[i]:
            continue
        while not mot2_matches[k]:
            k += 1
        if mot1[i] != mot2[k]:
            transpositions += 1
        k += 1
    #print ('Transpositions :',transpositions) #Console
    return ((matches / mot1_len) + (matches / mot2_len) + ((matches - transpositions/2) / matches)) / 3
 

    





"""
def levenshtein(mot1,mot2):
	ligne_i = [ k for k in range(len(mot1)+1) ]
	for i in range(1, len(mot2) + 1):
		ligne_prec = ligne_i
		ligne_i = [i]*(len(mot1)+1)
		for k in range(1,len(ligne_i)):	
			cout = int(mot1[k-1] != mot2[i-1])	
			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)	
	return ligne_i[len(mot1)]
	
"""




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
				if jaro(mot1, mot2) > 0.95:
                   			print(mot1,'    <>    ', mot2,' : ', jaro(mot1, mot2))
					#print(mot1,'    <>    ',mot2,' : ',levenshtein(mot1,mot2))
os.remove("newBNF_utf-8.txt")
os.remove("newBNF_utf-8.txt")



