# gestionnaire eleves
from operator import itemgetter
import json
import os

"""-----------------------Base-----------------------------------------------------------------------------------------
ajouter un eleve
ajouter une note
afficher les notes
calculer la moyenne
afficher tous les eleves


-----------niveau1-----------------------------------------------------------------------------------------------------
supprimer un eleve
modifier une note
afficher la meilleure note


-----------niveau2-----------------------------------------------------------------------------------------------------
afficher la moyenne de toute la classe
afficher l'eleve ayant la meilleure moyenne 
trier les eleves par moyenne


-----------niveau3-----------------------------------------------------------------------------------------------------
sauvegarder les donnees dans un fichier json
charger automatiquement les donnees au demarrage


-----------niveau4-----------------------------------------------------------------------------------------------------
generer un bulletin
quitter
"""

#------------------------------Niveau 3: Sauvegarde et chargement des données------------------------------------------
def sauvegarder_donnees(liste,fichier="eleve.json"):
    with open(fichier,"w", encoding="utf-8") as f:
        json.dump(liste, f, indent=4, ensure_ascii=False)
        print("Données sauvegardées dans le fichier JSON!\n")
    

def charger_donnees(fichier="eleve.json"):
    if os.path.exists(fichier):
        with open(fichier,"r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}
#--------------------------Fin Niveau 3--------------------------------------------------------------------------------


#-----------------Verification des matieres et chargement--------------------------------------------------------------
matieres_avec_coefficient=charger_donnees("matiere.json")

def verifier_matiere():
    if not matieres_avec_coefficient:
        print("Erreur : matiere.json est vide.")
        exit()
    else:
        matiere=input("Entrer le nom de la matière:")
        while(matiere not in matieres_avec_coefficient):
            print(f"{matiere} est une matière invalide dans cette section.")
            matiere=input("Entrer à nouveau le nom de la matière:")
        return matiere
#---------------Fin Verification---------------------------------------------------------------------------------------


#---------------Menu---------------------------------------------------------------------------------------------------
def afficher_menu():
    print("\n=== Gestionnaire des notes ===")
    print("1. Ajouter un élève")
    print("2. Ajouter une note")
    print("3. Afficher les notes")
    print("4. Calculer la moyenne")
    print("5. Afficher tous les élèves")
    print("6. Supprimer un élève")
    print("7. Modifier une note")
    print("8. Afficher la meilleure note")
    print("9. Afficher la moyenne de toute la classe")
    print("10. Afficher l'élève ayant la meilleure moyenne")
    print("11. Trier les élèves par moyenne")
    print("12. Générer un bulletin")
    print("13. Quitter le programme")
#-----------------------Fin Menu---------------------------------------------------------------------------------------



# Definition des fonctions necessaires -----------------Base-----------------------------------------------------------
def ajouter_eleve(liste):
    nom=input("Entrer le nom de l'élève:")
    if nom in liste:
        print("Cet élève existe déjà.")
        return
    else:
        liste[nom]={}
        print("Nouvel élève ajouté avec succès.")
        return


def ajouter_note(liste):
    nom=input("Entrer le nom de l'élève:")
    if nom not in liste:
        print(f"{nom} n'existe pas dans la liste.\n")
        return
    else:
        matiere=verifier_matiere()
        while True:
            try:
                note_matiere = float(input("Entrer la note : "))

                if note_matiere <= 0 or note_matiere > 20:
                    print("Note invalide.")
                    continue

                break

            except ValueError:
                print("Format incorrect.")
        liste[nom][matiere]=note_matiere
        print("Note ajoutée avec succès!\n")


def afficher_note(liste):
    nom=input("Entrer le nom de l'élève dont tu veux afficher les notes:")
    if nom not in liste:
        print(f"{nom} n'existe pas dans la liste.")
        return
    else:
        matiere=verifier_matiere()
        try:
            print(f"La note de l'élève \"{nom}\" en \"{matiere}\" est:")
            print(liste[nom][matiere])
        except KeyError:
            print(f"La note de \"{nom}\" pour \"{matiere}\" n'a pas été saisie!")
            print("Veuillez la saisir d'abord!\n")
            return
        

def calculer_moyenne_nom(liste, nom):

    if nom not in liste:
        return None

    notes = liste[nom]

    if not notes:
        return None

    somme = 0
    total_coef = 0

    try:
        for matiere, note in notes.items():
            somme += note * matieres_avec_coefficient[matiere]
            total_coef += matieres_avec_coefficient[matiere]
    except KeyError:
        return None
    else:
        return nom, somme / total_coef


def verifier_moyenne(moyenne):
    if(moyenne is None):
        print("Élève introuvable ou aucune note enregistrée.\n")
        return
    else:
        print(f"{moyenne[0]} a pour moyenne {moyenne[1]:.2f}\n")
        return


def calculer_moyenne(liste):
    nom=input("Entrer le nom de l'élève:")
    moyenne=calculer_moyenne_nom(liste, nom)
    verifier_moyenne(moyenne)


def afficher_eleves(liste):
    if len(liste)==0:
        print("Aucun élève dans la liste pour le moment.")
        return
    else:
        print("Les élèves présents dans la liste sont:")
        for nom in liste:
            print("-",nom)
#---------------------Fin Base-----------------------------------------------------------------------------------------


#------------------Niveau 1--------------------------------------------------------------------------------------------
def supprimer_eleve(liste):
    nom=input("Entrer le nom de l'élève que tu veux supprimer de la liste:")
    if nom not in liste:
        print(f"\"{nom}\" n'existe pas dans la liste.")
        return
    else:
        del liste[nom]
        print(f"\"{nom}\" a bien été supprimé de la liste.\n")
        return


def modifier_note(liste):
    nom=input("Entrer le nom de l'élève dont tu veux modifier la note:")
    if nom not in liste:
        print(f"\"{nom}\" n'existe pas dans la liste.\n")
        return
    elif len(liste[nom])==0:
        print(f"Veuillez d'abord insérer une note, aucune note n'a été insérée pour \"{nom}\".\n")
        return
    else:
        matiere=verifier_matiere()
        if(matiere not in liste[nom]):
            print(f"La note pour \"{matiere}\" n'a même pas été insérée, veuillez l'insérer avant de procéder à sa modification.\n")
            return
        else:
            while True:
                try:
                    note_matiere = float(input("Entrer la note : "))

                    if note_matiere <= 0 or note_matiere > 20:
                        print("Note invalide.")
                        continue

                    break

                except ValueError:
                    print("Format incorrect.")
            liste[nom][matiere]=note_matiere
            print("La note a bien été modifiée.")


def afficher_meilleure_note(liste):
    nom=input("Entrer le nom de l'élève dont tu veux afficher la meilleure note:")
    if nom not in liste:
        print(f"\"{nom}\" n'existe pas dans la liste.")
        return
    elif len(liste[nom])==0:
        print(f"\"{nom}\" n'a pas encore de notes disponibles.")
        return
    else:
        matieres=liste[nom]
        
        matiere,note=max(matieres.items(), key=lambda x: x[1])
        print((f"La meilleure note de \"{nom}\" est:\"{note}\" et est obtenue en \"{matiere}\"\n"))
#----------------------------------Fin Niveau 1------------------------------------------------------------------------


#------------------------------Niveau 2--------------------------------------------------------------------------------
def afficher_moyenne_classe(liste):
    if len(liste)==0:
        print("Liste d'élèves vides!")
        return
    else:
        for nom in liste:
            moyenne=calculer_moyenne_nom(liste, nom)
            verifier_moyenne(moyenne)
                
        
def afficher_meilleure_moyenne_eleves(liste):
    moyennes=[]
    for nom in liste:
        moyenne=calculer_moyenne_nom(liste, nom)

        if moyenne is not None:
            moyennes.append(moyenne)

    if not moyennes:
        print("Aucune moyenne disponible.")
        return

    meilleure_moyenne=max(moyennes,key=itemgetter(1))
    print(f"La meilleure moyenne est obtenue par {meilleure_moyenne[0]}: Moy={meilleure_moyenne[1]:.2f}\n")
    return
            
        
def trier_eleves_par_moyenne(liste):
    moyennes=[]
    for nom in liste:
        moyenne=calculer_moyenne_nom(liste, nom)
        if moyenne is not None:
            moyennes.append(moyenne)
    moyennes.sort(key=lambda x:x[1], reverse=True)
    ordre=1
    if moyennes:
        print("Les élèves classés par ordre de mérite sont:")
        for elvs_classes in moyennes:
            print(f"{ordre}). {elvs_classes[0]}: Moyenne={elvs_classes[1]:.2f}")
            ordre+=1
        return
    else:
        print("La liste d'élèves est vide!")
        print("Veuillez la remplir d'abord!")
        return
#--------------------------Fin Niveau 2--------------------------------------------------------------------------------


#------------------------------Niveau 4--------------------------------------------------------------------------------
def obtenir_mention(moyenne):
    match(moyenne):
            case x if 10<=x<=11.99:mention="Passable"
            case x if 12<=x<=13.99:mention="Assez-Bien"
            case x if 14<=x<=15.99:mention="Bien"
            case x if 16<=x<=17.99:mention="Très-Bien"
            case x if 18<=x<=19.99:mention="Excellente"
            case _:mention="Insuffisante"
    return mention

def generer_bulletin(liste):
    nom=input("Entrer le nom de l'élève:")
    moyenne=calculer_moyenne_nom(liste,nom)

    if moyenne is None:
        print(f"Impossible de générer le bulletin de \"{nom}\", élève introuvable ou note non enregistrée.\n")
        return
    else:
        notes=liste[moyenne[0]]
        print(f"\nNom : {moyenne[0]}\n")
        print("Notes : ")

        for matiere in notes:
           print(f"{matiere} : {liste[moyenne[0]][matiere]}")
        moyenne=moyenne[1]

        mention=obtenir_mention(moyenne)
        print(f"\nMoyenne : {moyenne:.2f}")
        print(f"Mention : {mention}\n")
        return
#--------------------------Fin Niveau 4--------------------------------------------------------------------------------


#-------------------------Sauvegarde et arret du programme
def quitter(liste):
    sauvegarder_donnees(liste,fichier="eleve.json")
    print("Fin du programme")
    return

#----------------------------------------------------------------------------------------------------------------------


#Programme principal
if __name__=="__main__":
    eleves=charger_donnees(fichier="eleve.json")

    while True:
        afficher_menu()
        try:
            choix=int(input("Entrer le numéro de l'operation à effectuer:"))
        except ValueError:
            print("Le choix doit être un entier.\nVeuillez réessayer une entrée valide:")
        else:
            match(choix):
                case 1:ajouter_eleve(eleves)
                case 2:ajouter_note(eleves)
                case 3:afficher_note(eleves)
                case 4:calculer_moyenne(eleves)
                case 5:afficher_eleves(eleves)
                case 6:supprimer_eleve(eleves)
                case 7:modifier_note(eleves)
                case 8:afficher_meilleure_note(eleves)
                case 9:afficher_moyenne_classe(eleves)
                case 10:afficher_meilleure_moyenne_eleves(eleves)
                case 11:trier_eleves_par_moyenne(eleves)
                case 12:generer_bulletin(eleves)
                case 13:
                    quitter(eleves)
                    break
                case _:print("Opération invalide, réessayer!")