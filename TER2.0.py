#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re, os, sys, cgi,os.path
from os.path import basename, splitext

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////// TER 2.0 /////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////// PROGRAMME QUI GENERE UN  FICHIER  RETOUR.RDF  CONTENANT  QUE  LES RELATIONS ///////////////////////////////
#///////////////////// VALIDES  DONT  L'ARGUMENT ENTITY1  OU  ENTITY2  EST PRESENT AU MINIMUM DEUX ///////////////////////////////
#///////////////////// FOIS, EXPORTATION AUTOMATIQUE DES FICHIERS RETOUR AVEC LE NOM D'ORIGINE+_DB ///////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////// UTILISATION CODE : VEUILLEZ COPIER COLLER LE CODE TER.PY DANS LE DOSSIER CONTENANT LES FCHIERS .RDF ////////////////
#////////////////// ET L'EXECUTER A L'AIDE DE L'INVITÉ DE COMMANDE AVEC DROITS D'ECRITURE ET DE MODIFICATION /////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#///////////////////////Lecture et création des fichiers (fichier de base + _DB)://///////////////////////////////////////////////

rep=os.getcwd() #récupérer le dossier courant 

print('\n'+'Dossier courant :'+rep+'\n') #Console :suivi
newRep=rep.split('\\')[-1]+'_DB'

if not os.path.exists(newRep):    #Vérification des fichiers et dossiers et création du dossier contenant les retour_DB
    os.mkdir(newRep)

liFichiers = os.listdir(rep) #Listing du contenu du répertoire courant (ONLY .RDF FILES) que le code va traiter

print('liste des fichiers à traiter :')
for fichier in liFichiers:
	if fichier.endswith('.rdf'):
		print(fichier)
print('\n')


#explorer tout le contenu du dossier courant et appliquer le traitement pour chaque fichier.rdf dedans
print('Liste des fichiers retour créés :') 	
listeNomsFichiers={} #Utilisation d'un dictionnaire 
for fichier in liFichiers:
	print('\n'+'Traitement de :'+fichier)
	
	fDispo = re.search("(.*)\.rdf", fichier)
	if fDispo:
		filepath=(fDispo.group(1)+'.rdf')
		if filepath not in listeNomsFichiers:
			listeNomsFichiers[filepath] = fichier
		
			fichierRdf = open(filepath) #chemin
			lecture = fichierRdf.read() #lecture fichier 1
			filename = splitext(basename(filepath))[0]
			fichieRetour = open(newRep+'/'+filename+'_DB.rdf','x') #création fichier de retour_DB.rdf
			
			
			print(filename+'_DB.rdf : créé dans '+newRep+'  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< :D'+'\n') #Console: Validation création fichier de retour_DB.rdf

			newF = open('newF','x') #nouveau fichier temporaire 1



#///////////////////////  Rajouter le début du code XML   ///////////////////////////////////////////////////////////////////////



			debut = re.compile(r".*(\<\?xml.*\s+\<rdf.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+\<Alignment.*\s+\<xml.*\s+\<level.*\s+\<type.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*\s+.*).*") 
			# début code XML

			res1 = re.search(debut,lecture)

			if res1:
				a = res1.group(1)
	
				fichieRetour.write(a)	#ecriture du début sur le fichier retour
			else:
				print('Pas de correspondance lors de la récupération de l\'entête, verifier le code source SVP!')

#///////////////////////  Recupérer les relations valides   ////////////////////////////////////////////////////////////////////



			corps = re.compile(r".*(\s+\<map\>\s+\<Cell\>\s+.*\s+.*\s+.*exactMatch.*\s+.*\s+\</Cell\>\s+\</map\>).*") #les relations valides uniquement

			res = corps.findall(lecture)

			if res:
				for ligne in res:
					newF.write(ligne) #ecriture des lignes valides dans un fichier tomporaire (newF)
			else:
				print('Pas de relations valides trouvées')
				
			
			
			newF.close() #femeture fichier temporaire 1





#///////////////////////  Rajouter aux liens présents >1 fois l'indicateur CIBLA   /////////////////////////////////////////////



			newF = open('newF','r') # exploiter temporaire 1 en lecture

			lecture2 = newF.read() #lecture fichier 1

			semiFinals = open('newF2','x') # création fichier tomporaire 2

			res2 = re.findall(".*rdf:resource='(.*)'/\>",lecture2) #identifier les liens
			
			m = list() # On crée une liste pour éviter d'afficher les mêmes lignes plusieurs fois (distinct)
			
			if res2:
				for line in res2:
					d = res2.count(line)
					if d > 1: # ce lien est présent au moins 2 fois
						avecCibla = lecture2.replace(line,line+'CIBLA')	#identifier les liens doublons avec le mot CIBLA
						semiFinals.write(avecCibla) # ecriture des lignes avec modifications sur le fichier temporaire 2
						if line not in m:
							print('lien présent :',line,':',d,' fois sauvegardé.') #Console : suivi
							m.append(line) # si la ligne n'existe pas dans m() alors l'ajouter.
						
						
				
				
			semiFinals.close() #femeture fichier temporaire 2
			
		



			print('Veuillez patienter SVP!'+'\n'+'ecriture de '+filename+'_DB.rdf en cours'+'\n')
			
			
#///////////////////////  Rajouter aux liens présents >1 fois l'indicateur <<CIBLA>>   /////////////////////////////////////////



			semiFinals = open('newF2','r') # exploiter temporaire 2 en lecture

			lecture3 = semiFinals.read() #lecture fichier 2

			semiFinals2 = open('newF3','x') # création fichier tomporaire 3
			
			#identifier les blocs <map>....</map> contenant 'CIBLA' >>>> ça nous permet de ne repérer que les blocs avec des liens présents au minimum 2fois
			res3 = re.findall(".*(\s+\<map\>\s+\<Cell\>\s+.*CIBLA'/\>\s+.*\s+.*\s+.*\s+\</Cell\>\s+\</map\>).*", lecture3) # resultat des blocs valides avec entity1 présents plusieurs fois
			res4 = re.findall(".*(\s+\<map\>\s+\<Cell\>\s+.*\s+.*CIBLA'/\>\s+.*\s+.*\s+\</Cell\>\s+\</map\>).*", lecture3) # resultat des blocs valides avec entity2 présents plusieurs fois

			if res3 :
				print('Liens entity1 présents au min 2 fois'+'\n')
				for ligne in res3:
					semiFinals2.write(ligne) # ecriture des lignes avec (entity1 > 2) sur le fichier temporaire 3
			else:
				print('Liens entity1 présents chacun une seule fois'+'\n')
				
			if res4 :
				print('Liens entity2 présents au min 2 fois'+'\n')
				for ligne in res4:
					semiFinals2.write(ligne) # ecriture des lignes avec (entity2 > 2) sur le fichier temporaire 3
			else:
				print('Liens entity2 présents chacun une seule fois'+'\n')
				
					
			semiFinals2.close() #femeture fichier temporaire 3

			print('\n')





#//////////////////////////////  Suppression de l'indicateur CIBLA  ////////////////////////////////////////////////////////////



			semiFinals2 = open('newF3','r') # exploiter temporaire 3 en lecture

			lignes = semiFinals2.readlines() #lecture fichier 3

			finals = open('newF4.rdf','x') # création fichier tomporaire 4

			for ligne in lignes:
				ligneFinale = ligne.replace('CIBLA','')	# parcourir les lignes du fichier tomporaire 3 et remplacer CIBLA par un vide''	
				finals.write(ligneFinale) # ecriture des lignes propres sur le fichier temporaire 4

			semiFinals2.close() #femeture fichier temporaire 3
			finals.close() #femeture fichier temporaire 4
			






#/////////////////////// Suppression des blocs doublons en respectant l'ordre des lignes du fichier ////////////////////////////

			s = list() #création d'une liste s vide
	
			finals = open('newF4.rdf','r') # exploiter temporaire 4 en lecture

			corps = re.compile(r".*(\s+\<map\>\s+\<Cell\>\s+.*\s+.*\s+.*exactMatch.*\s+.*\s+\</Cell\>\s+\</map\>).*")
			fichierF = finals.read()

			res = corps.findall(fichierF)
			if res:
				for line in res:
					if line not in s:
						s.append(line) # si la ligne existe dans s() alors l'ignorer.
						fichieRetour.write(line) # ecriture des lignes finales sur le fichier de retour_DB.rdf 

			finals.close() #femeture fichier temporaire 4
			





#///////////////////////  Rajouter le bas du code XML dans le fichier final et suppression des fichiers tmp ////////////////////

			res3 = re.search("(\s+</Alignment>\s+</rdf:RDF>)", lecture) 

			if res3:
				c = res3.group(1)
				fichieRetour.write(c) #ecriture des lignes du bas XML
				
				
			
			os.remove("newF")  #suppression fichier temporaire 1
			os.remove("newF2") #suppression fichier temporaire 2
			os.remove("newF3") #suppression fichier temporaire 3
			os.remove("newF4.rdf") #suppression fichier temporaire 4
			fichieRetour.close() #femeture fichier retour

#///////////////////////  Continuer à éxecuter le programme tant qu'on a tjrs des fichiers non traités  ////////////////////////
		else:
			listeNomsFichiers[filepath] += fichier
	else:
		print('fichier d\'une autre extension repéré, aucune action n\'est exécutée')

