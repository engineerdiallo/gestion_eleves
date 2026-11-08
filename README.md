# Gestion Interactive des Elèves 

## A propos de ce projet
Ce projet est un script interactif en Python conçu pour la gestion des élèves et de leurs notes.

**Note importante :** Il s'agit d'un projet d'apprentissage. Ce code, je l'ai dévéloppé quand j'ai débuté en Python; c'était donc un "bout d'essai" pour valider et assimiler les concepts fondamentaux du langage (boucles, conditions, listes/dictionnaires, fonctions, fichiers...)


## Fonctionnalités Intégrées
L'application fonctionne en ligne de commande avec une boucle interactive permettant de :
1. Ajouter un élève
2. Ajouter une note
3. Afficher les notes
4. Calculer la moyenne
5. Afficher tous les élèves
6. Supprimer un élève
7. Modifier une note
8. Afficher la meilleure note
9. Afficher la moyenne de toute la classe
10. Afficher l'élève ayant la meilleure moyenne
11. Trier les élèves par moyenne
12. Générer un bulletin
13. Quitter le programme

## Persistance des données (JSON)
Le projet intègre également la gestion de fichiers pour sauvegarder les données :
- "matiere.json": Stocke la configuration des matières disponibles et leurs coefficients.
- "eleve.json": Sauvegarde dynamiquement la liste des élèves et leurs notes (qui pourront être générées à l'exécution).

**Le fichier eleve.json** est utilisé automatiquement au lancement du programme s'il existe déjà, créé sinon.


## Comment exécuter le projet 
1. Clonez le dépôt : git clone https://github.com/engineerdiallo/gestion_eleves.git
2. Lancez le script : python gestion_eleves.py