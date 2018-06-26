# TER2018
Projet TER - Alignement des vocabulaires

Contenu du hub :

- Resultats tache 1: Traitement de données rdf
 - tache1_TERValid.py:
  Ce programme Python effectue un traitement sur plusieurs fichiers .rdf avec un format <xml> centenus dans le même dossier, il nous     permet de filtrer le contenu des fichiers de base de telle sorte qu'on ne garde à la fin que des balises <map></map> ne contenant que des relations <relation.*exacteMatch.*>.
Les résultats sont inscrits dans des fichiers appelés doublons, ayant le même nom que l'original avec _DB comme suffixe.
  
  Nous avons utilisé, durant l'élaboration de ce code, les modules re, sys, os, os.path, splitext et basename, à l'aide de plusieurs REGEX (expression régulière) visant en boucle les balises <map>.*</map> et ensuite à l'intérieur de chaque bloc de balises la mention .*exactMatch.*
Un exemple des résultats est présent dans le dossier. (avec la mention _DB)



- Resultats tache 2: Alignement des vocabulaires (BNF : Bibliothèque Nationale de France, et RAMEAU : Radio France)

 - tache2_prepaFichiers.py:                       ETAPE 01
 Avec ce programme Python, nous allons préparer les fichiers d'alignement cette opération consiste à l'application de plusieurs traitements aux chaines de caractère à aligner;
Tokénization
Lemmatization
Suppression de STOP-WORDS (en français) et autres mots inutiles (peuples....)
Structuration des informations dans les deux nouveaus fichiers : ID~STRING
 - newRameau_utf-8.txt : contenant des informations sur le peuple et/ou sa géographie.
 - newBNF_utf-8.txt : contenant les informations sur l'éthnie et/ou sa géographie.
 
 - tache2_Alignement_BNF_RAMEAU_jaro.py:             ETAPE 02
  Ici ce fera l'alignement des termes entre les deux vocabulaires (BNF/RAMEAU) en se basant sur deux mesures de similarité principales : 
Levenshtein et Jaro-Winkler, 
  Nous avons donc à l'aide des boucles pu parcourir les bases BNF/RAMEAU et avons extrait les informations liées à l'éthni/ peuple et leur position géographique si disponnibles, afins de mesurer la similiratité entre les termes, comme exemple, dans le fichier Retour/ethnieRegionMatch.csv on retrouve que le peuple RAMEAU [38471794	$aTraditions$mOcéanie$mAustralie$eNyongaar] est aligné avec	l'ethnie BNF [12045606	$aNyungar$gpeuple d'Australie] et dont la similarité est de Score=0.823.

  Trois cas de figures sont possibles:
- ethnieRegionMatch.csv : contenant des alignements double sens, c'est à dire que les deux termes possèdent des informations de géographie (position dans le monde) (1), et que l'ethnie BNF valide le seuil de similarité avec le peuple RAMEAU (2), et leur régions respectives aussi (3).
- ethnieMatch.csv : contenant des alignements d'ethnie, pour le cas de termes présents parfois sans informtion géographique.
- ethnieErrosMatch.csv : ici les résultats sont à 50% justes, des cas d'ambiguité nous font surface par moment, comme pour le cas de [41073209	$aTraditions$mAfrique$mTanzanie$eGogo] qui est aligné avec [13514558	$aGogo$gpeuple d'Afrique] et dont la similarité est de Score:1.0 , dans ce cas là, on voit l'ethnie $aGogo parfaitement alignée avec le peuple $eGogo, tous les deux ont comme continent l'Afrique mais l'un d'eux possède une précision de Pays $mTanzanie...

Au final, nous rajoutons un fichier nommé : bnfNotMatch.csv contenant les termes BNF qui n'ont pas pu valider aucun seuil et sont donc rejetés et non alignés.

Pour plus de détails, veuillez consulter le corps du code PYTHON en question commenté, et vous y trouverez le descriptif de toutes les étapes dans le détail.


- Resultats tache 3:

Vous trouverez des README pour chaque tâche dans le dossier spécifié.

M1S2 2017/2018
N.Bendjoudi, I.Djerroud, W.Keblouti.

Projet encadré par : 
K.Todorov



