#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#chaine simple :

#entre : Bon – Pont

#remplacer
  >>> s = "Bon"
  >>> s = s[:0] + "P" + s[1:]
  >>> print (s)
  'Pon'


#Ajouter

  >>> s = "Bon"
  >>> s = s[:3] + "t" 
  >>> print(s)
  Bont
  #La distance d'edit Levenstein ici est 2 >>>>> le résultat (2) c'est le nombre minimal de remplacements ou de modification





# la méthode levenstein en python, calculant le nombre minimale de modification entre deux chaine de caractères:

def LevDistance(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LevDistance(s[:-1], t)+1,
               LevDistance(s, t[:-1])+1, 
               LevDistance(s[:-1], t[:-1]) + cost])
    return res
print(LD("Bon", "Pont"))

2


# chaine décomposée en sous chaines:  Maison - Raison ( distance.levenshtein est une méthode prédefinie )

>>> t1 = ("ma", "is", "on")
>>> t2 = ("ra", "is", "on")
>>> distance.levenshtein(t1, t2)

1


#chaine complexe 

>>> ch1 = ['je', 'suis', 'etudiant', 'en', 'master','informatique','pour','science']
>>> ch2 = ['je', 'suis', 'etudiant', 'a', 'la fac', 'informatique']
>>> distance.levenshtein(sent1, sent2)
4









#//DISTANCE LEVENSHTEIN/////////////////////////////////////////////////////////////////////////////////////////////////////

def levenshtein(mot1,mot2):
	# ligne_i est un tableau tel que tout au long de l'algorithme,
	# ligne_i[k] contienne la distance de levenshtein entre les k premières lettres de mot1
	# et les i premières lettres de mot2
	# Au début, i=0, et la distance entre les k premières lettres de mot1 et la chaîne vide
	# vaut bien sûr k. (il faut faire k suppressions pour passer des k premières lettres de mot1
	# à la chaîne vide)
	ligne_i = [ k for k in range(len(mot1)+1) ]
	# i va ensuite varier de 1 à len(mot2)
	for i in range(1, len(mot2) + 1):
		# i vient d'être incrémenté. On stocke dans ligne_prec la valeur de la ligne numéro i-1
		ligne_prec = ligne_i
		# On crée la nouvelle ligne, dont le premier élément (l'élement numéro 0) doit être
		# la distance de levenshtein entre la chaîne vide ("") et les i premières lettres de mot2, soit i
		# (il faut faire i additions pour passer de la chaîne vide aux i premières lettres de mot2)
		ligne_i = [i]*(len(mot1)+1)
		# On va ensuite remplir le reste de la ligne i, c'est-à-dire calculer ligne_i[k] pour k allant de 1 à len(mot1)
		for k in range(1,len(ligne_i)):
			# La variable cout vaut 0 si la kième lettre de mot1 est la même que la ième lettre de mot2, et 1 sinon
			#La kième lettre de mot1 s'obtient avec mot1[k-1], les indices commencent à 0
			cout = int(mot1[k-1] != mot2[i-1])
			#Voilà enfin le sel de l'algorithme, le calcul de ligne_i[k] pour i et k quelconques,
			# connaissant ligne_prec[k-1], ligne_prec[k] et ligne_i[k-1]
			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
			# Lorsque l'on sort de la boucle, i vaut len(mot2)
			#Ce que l'on cherche est la distance de levenshtein entre les len(mot1) premières lettres de mot1
			# et les len(mot2) premières lettres de mot2, qui est stockée dans ligne_i[len(mot1)]
	return ligne_i[len(mot1)]
	
print (levenshtein("nassim", "nassims"))
