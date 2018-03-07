#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#//DISTANCE JARO/////////////////////////////////////////////////////////////////////////////////////////////////////



from __future__ import division
 
def jaro(s, t): #s et t étant les chaines de caractère à aligner
    s_len = len(s) #s_len est le nombre de caractères dans s
    t_len = len(t) #t_len est le nombre de caractères dans t
 
    if s_len == 0 and t_len == 0: # si il n y a pas de lettres dans les deux mots, alors retourner la valeur 1 comme distance JARO
        return 1
 
    match_distance = (max(s_len, t_len) // 2) - 1 # on calcul la moitié de la distance du max des longueurs de s ou t et on soustrait cette valeur à 1
    
    print('\n','Match_distance :',match_distance) #Console 
    
    s_matches = [False] * s_len 
    t_matches = [False] * t_len
 
    matches = 0
    transpositions = 0
 



    for i in range(s_len): #on parcours s
        start = max(0, i-match_distance) #start est le max entre 0 et la valeur de i-match_distance
        end = min(i+match_distance+1, t_len) #end est le min entre i+match_distance et la longueur de t
 
        for j in range(start, end): #
            if t_matches[j]:
                continue
            if s[i] != t[j]:
                continue
            s_matches[i] = True
            t_matches[j] = True
            matches += 1
            break
 
    if matches == 0:
        print('Matche :',0)
        return 0
    print ('Matches :',matches) #Console




    k = 0
    for i in range(s_len):
        if not s_matches[i]:
            continue
        while not t_matches[k]:
            k += 1
        if s[i] != t[k]:
            transpositions += 1
        k += 1
    print ('Transpositions :',transpositions) #Console
    return ((matches / s_len) + (matches / t_len) + ((matches - transpositions/2) / matches)) / 3
 
for s,t in [('nassim','bokle'),('undeuxtrois','undeux'),('hope','hopes'),('SPI','SpI'),('ips','ips'),('chien','niche')]:
    print("jaro(%r, %r) = %.10f" % (s, t, jaro(s, t)))
