import datetime
import json

salaire = 0
prime = 0
complement_revenu = 0
depenses = 0
argent_net = 0
prelevements_globaux = []
reserves_input = 0
reserves = 0  
retrait = 0
reserves_inputneg = 0
reserves_inputpos = 0
depense = 0



def enregistrer_donnees_texte(nom_fichier):
    global salaire, prime, prelevements_globaux, argent_net, depenses_possibles, complement_revenu, depenses, argent_disponible, reserves, reserves_input
    donnees = {
        "salaire": salaire,
        "prelevements_globaux": prelevements_globaux,
        "argent_net": argent_net,
        "depenses_possibles": depenses_possibles,
        "prime": prime,
        "complement_revenu": complement_revenu,
        "depenses": depenses,
        "argent_disponible": argent_disponible,
        "reserves": reserves,
        "reserves_input": reserves_input 
    }
    with open(f"{nom_fichier}.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)



def lire_donnees_texte(nom_fichier):
    global salaire, prelevements_globaux, argent_net, depenses_possibles, prime, complement_revenu, depenses, argent_disponible, reserves
    try:
        with open(f"{nom_fichier}.json", "r") as fichier:
            donnees = json.load(fichier)
            salaire = donnees.get("salaire", 0)
            prelevements_globaux = donnees.get("prelevements_globaux", [])
            argent_net = donnees.get("argent_net", 0)
            depenses_possibles = donnees.get("depenses_possibles", 0)
            prime = donnees.get("prime", 0)
            complement_revenu = donnees.get("complement_revenu", 0)
            depenses = donnees.get("depenses", 0)
            argent_disponible = donnees.get("argent_disponible", 0)
            reserves = donnees.get("reserves", 0)
    except FileNotFoundError:
        print("Fichier de données introuvable. Création d'un nouveau fichier.")
        salaire = 0
        prelevements_globaux = []
        argent_net = 0
        depenses_possibles = 0
        prime = 0
        complement_revenu = 0
        depenses = 0
        argent_disponible = 0
        reserves = 0
        enregistrer_donnees_texte(nom_fichier)  
    except json.JSONDecodeError:
        print("Erreur lors de la lecture des données. Format de fichier incorrect.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

def charger_donnees_mois(nom_fichier):
    mois = input("entrez le mois des donnees à charger ex Janvier-2024")
    lire_donnees_texte(mois)




def menu_salaire(nom_fichier):
    while True:
        print("\nMenu Salaire\n")
        print("1. Entrer le salaire reçu")
        print("2. Entrer une prime reçue")
        print("3. Entrer un complément au salaire")
        print("4. Corriger une erreur")
        print("5. Quitter\n")
        try:
            argent_dispo = calculer_argent_disponible()  
            print(f"Vous avez {argent_dispo} € de disponible")
        except Exception as e:
            print(f"Une erreur est survenue lors du calcul de l'argent disponible: {e}")
        
            continue

        try:
            choix = int(input("Choisissez une catégorie : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choix == 1:
            salaire_reçu(nom_fichier)
        elif choix == 2:
            prime_reçue(nom_fichier)
        elif choix == 3:
            complement(nom_fichier)
        elif choix == 4:
            corriger_erreur(nom_fichier)
        elif choix == 5:
            print("Quitter le menu Salaire.")
            break
        else:
            print("Option non valide, veuillez choisir un numéro entre 1 et 5.")



def salaire_reçu(nom_fichier):
    global salaire
    global argent_net
    while True:
        try:
            salaire_input = input("Combien avez-vous reçu ? :")
            salaire_temp = float(salaire_input) 
            if salaire_temp < 0:
                print("Le montant du salaire ne peut pas être négatif. Veuillez entrer un montant valide.")
                continue
            salaire = salaire_temp
            break  
        except ValueError:
            print("Veuillez entrer un nombre valide. Par exemple, 2500.50")
            

    print("Prise en compte de votre salaire...")
    argent_net += salaire  

    enregistrer_donnees_texte(nom_fichier)  


def prime_reçue(nom_fichier):
    global prime
    global argent_net

    while True:
        try:
            prime_input = input("Combien avez-vous reçu en prime ? :")
            prime_temp = float(prime_input)  
            if prime_temp < 0:
                print("Le montant de la prime ne peut pas être négatif. Veuillez entrer un montant valide.")
                continue
            prime = prime_temp
            break  
        except ValueError:
            print("Veuillez entrer un nombre valide. Par exemple, 500.00")
            
    print("Prise en compte de votre prime...")
    argent_net += prime  

    enregistrer_donnees_texte(nom_fichier)  

def complement(nom_fichier):
    global argent_net
    global complement_revenu

    while True:
        try:
            complement_input = input("Combien avez-vous eu en complément ? :")
            complement_temp = float(complement_input)  
            if complement_temp < 0:
                print("Le montant du complément ne peut pas être négatif. Veuillez entrer un montant valide.")
                continue
            complement_revenu = complement_temp
            break  
        except ValueError:
            print("Veuillez entrer un nombre valide. Par exemple, 300.00")
            
    print("Prise en compte de votre complément...")
    argent_net += complement_revenu  

    enregistrer_donnees_texte(nom_fichier)  



def corriger_erreur(nom_fichier):
    global argent_net

    while True:
        try:
            erreur_input = input("Combien voulez-vous enlever à votre argent disponible ? : ")
            erreur = float(erreur_input)
            argent_disponible_apres_prelevements = calculer_argent_disponible()

            if erreur < 0:
                print("Le montant ne peut pas être négatif. Veuillez entrer un montant valide.")
            elif erreur > argent_disponible_apres_prelevements:
                print(f"Le montant ne peut pas dépasser votre argent disponible après prélèvements, qui est de {argent_disponible_apres_prelevements} €.")
            else:
                break  
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    argent_net -= erreur  
    print(f"Vous avez donc {calculer_argent_disponible()} € disponible après cette correction.")

    enregistrer_donnees_texte(nom_fichier)



def menu_prelevements(nom_fichier):
    while True:
        print("\nMenu des prélèvements\n")
        print("1. Ajouter un prélèvement")
        print("2. Supprimer un prélèvement")
        print("3. Voir les prélèvements")
        print("4. Retour au menu principal")

        choix = input("Choisissez une option : ")

        try:
            choix = int(choix)

            if choix == 1:
                ajouter_prelevements(nom_fichier)
            elif choix == 2:
                nom_prelevement = input("Entrez le nom exact du prélèvement que vous voulez supprimer ou entrez 'q' pour quitter : ")
                if nom_prelevement.lower() == "q":
                    print("Retour au menu principal...")
                else:
                    supprimer_prelevement(nom_prelevement,nom_fichier)
            elif choix == 3:
                afficher_prelevements(nom_fichier) 
            elif choix == 4:
                print("Retour au menu principal...")
                break
            else:
                print("Option non valide. Veuillez choisir un nombre entre 1 et 4.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre. Veuillez réessayer.")






def ajouter_prelevements(nom_fichier):
    while True:
        nom = input("Entrez le nom du prélèvement ou 'q' pour quitter : ").strip().lower()
        
        if nom == "q":
            print("Retour au menu précédent...")
            break
        
        montant_str = input("Entrez le montant du prélèvement ou 'q' pour quitter : ").strip().lower()
        
        if montant_str == "q":
            print("Retour au menu précédent...")
            break
        
        try:
            montant = float(montant_str)
            
            if montant < 0:
                print("Le montant du prélèvement ne peut pas être négatif. Réessayez.")
                continue  
                
            prelevements_globaux.append({'nom': nom, 'montant': montant})
            print(f"Prélèvement '{nom}' de {montant} € ajouté avec succès.")
            enregistrer_donnees_texte(nom_fichier)
            break
        
        except ValueError:
            print("Veuillez entrer un montant valide (nombre). Réessayez.")





def supprimer_prelevement(nom_prelevement,nom_fichier):
    global prelevements_globaux
    prelevements_avant = prelevements_globaux.copy()  

    
    prelevements_globaux = [prelevement for prelevement in prelevements_globaux if prelevement['nom'] != nom_prelevement.lower()]

    
    if len(prelevements_avant) == len(prelevements_globaux):
        print(f"Aucun prélèvement avec le nom '{nom_prelevement}' trouvé.")
    else:
        print(f"Prélèvement '{nom_prelevement}' supprimé si existant.")
        enregistrer_donnees_texte(nom_fichier)


def afficher_prelevements(nom_fichier):
    if prelevements_globaux:
        print("\nListe des prélèvements :")
        for prelevement in prelevements_globaux:
            print(f"Nom: {prelevement['nom'].capitalize()}, Montant: {prelevement['montant']} €")
    else:
        print("\nAucun prélèvement n'a été ajouté.")

    input("\nAppuyez sur Entrée pour continuer...")


    



def calcul_depenses(nom_fichier):
    global argent_net, prelevements_globaux ,depense,depenses
    
    while True:
        argent_disponible = calculer_argent_disponible()  
        print(f"Vous avez {argent_disponible} € de disponible.")
        depense_input = input("Combien as-tu dépensé ? (Appuyez sur 'q' pour quitter) : ")
        
        if depense_input.lower() == "q":  
            break  

        try:
            depense = float(depense_input)
            if depense <= argent_disponible:  
                argent_net -= depense  
                depenses += depense
                enregistrer_donnees_texte(nom_fichier)
            else:
                print("Dépense refusée. Vous n'avez pas assez d'argent disponible.")
        except ValueError:  
            print("Entrez une valeur valide ou 'q' pour quitter.")




def remise_a_zero(nom_fichier):
    global salaire, prime, argent_net, depenses_possibles, prelevements_globaux, complement_revenu,depenses,depense
    mois = input("Entrez le mois : ")
    nom_fichier = mois
    salaire = 0
    argent_net = 0
    depenses_possibles = 0
    prelevements_globaux = []
    complement_revenu = 0
    depenses = 0
    depense = 0

    print("Données réinitialisées. Bienvenue dans votre nouveau mois, ne dépensez pas trop :)")

    enregistrer_donnees_texte(mois)


def calculer_argent_disponible():
    global argent_net, prelevements_globaux, reserves_input

    total_prelevements = sum(prelevement['montant'] for prelevement in prelevements_globaux)
    argent_disponible = argent_net - total_prelevements 


    return argent_disponible





import datetime

import datetime

def calcul_objectif_argent():
    while True:
        try:
            reserves = float(input("Combien avez-vous déjà mis d'argent de côté ? "))
            if reserves < 0:
                raise ValueError("Le montant des réserves ne peut pas être négatif.")

            objectif = float(input("Combien d'argent souhaitez-vous mettre de côté au total ? "))
            if objectif < 0:
                raise ValueError("L'objectif d'économie ne peut pas être négatif.")

            annee_estimation = int(input("Jusqu'à quelle année souhaitez-vous estimer vos économies ? "))
            now = datetime.datetime.now()
            if annee_estimation <= now.year:
                raise ValueError("L'année d'estimation doit être dans le futur.")

            mois_restants = (annee_estimation - now.year) * 12
            if mois_restants <= 0:
                raise ValueError("Nombre de mois restants invalide.")

            objectif_restant = objectif - reserves
            montant_mensuel = objectif_restant / mois_restants
            argent_mis_de_cote = montant_mensuel * mois_restants

            print(f"Pour atteindre votre objectif de {objectif} € d'ici l'année {annee_estimation},")
            print(f"avec {reserves} € déjà mis de côté, vous devez économiser environ {montant_mensuel:.2f} € par mois.")
            print(f"Cela vous permettra d'avoir environ {argent_mis_de_cote:.2f} € d'économies.")
            break
        except ValueError as ve:
            print(f"Erreur : {ve}")
        except Exception as e:
            print(f"Une erreur inattendue est survenue : {e}")

def reserves_argent(nom_fichier):
    global reserves, argent_disponible,reserves_input,argent_net
    
    print(f"Vous avez {reserves} € de côté.")
    
    while True:
        action = input("Que voulez-vous faire?\n"
                       "1. Ajouter de l'argent\n"
                       "2. Retirer de l'argent\n"
                       "q. Quitter\n"
                       "Choisissez une option : ")
        
        if action == 'q':
            break
        elif action == '1':
            try:
                reserves_input = float(input("Combien d'argent voulez-vous mettre de côté ce mois-ci : "))
                
                reserves = reserves + reserves_input
                argent_net = argent_net - reserves_input
            
                print(f"Votre nouveau solde de côté est de {reserves} €.")
                enregistrer_donnees_texte(nom_fichier)
                reserves_input = 0
            except ValueError:
                print("Erreur : Veuillez entrer un montant valide.")


        elif action == '2':
            try:
                reserves_input = float(input("Combien d'argent voulez-vous retirer: "))
                
                reserves = reserves - reserves_input
                argent_net = argent_net + reserves_input
            
                print(f"Votre nouveau solde de côté est de {reserves} €.")
                enregistrer_donnees_texte(nom_fichier)
                
            except ValueError:
                print("Erreur : Veuillez entrer un montant valide.")



def afficher_totals(nom_fichier):
    total_prelevements = sum(prelevement['montant'] for prelevement in prelevements_globaux)
    total_depenses = depenses

    print(f"\nTotal des prélèvements pour le mois : {total_prelevements} €")
    print(f"Total des dépenses pour le mois : {total_depenses} €\n")
    print(f"Total entrés d'argent pour le mois {salaire + prime + complement_revenu} €")


def menu(nom_fichier):
    while True:
        print("\nMenu Principal\n")
        print("Options :")
        print("1. Gérer les entrées d'argent")
        print("2. Gérer les prélèvements")
        print("3. Calculer des prévisions d'économies")
        print("4. Ajouter ou supprimer une dépense")
        print("5. Commencer un nouveau mois / Remise à zéro")
        print("6. Ajouter / Supprimer de l'argent de côté")
        print("7. Charger les données d'un ancien mois")
        print("8. Afficher vos prélèvements et depenses")
        print("0. Quitter le programme\n")

        argent_dispo = calculer_argent_disponible()  
        print(f"Vous avez {argent_dispo} € de disponible")

        choix = input("Sélectionnez une option en entrant le numéro correspondant : ")
        
        if choix == "0":
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break
        elif choix == "1":
            menu_salaire(nom_fichier)
        elif choix == "2":
            menu_prelevements(nom_fichier)
        elif choix == "3":
            calcul_objectif_argent()
        elif choix == "4":
            calcul_depenses(nom_fichier)
        elif choix == "5":
            remise_a_zero(nom_fichier)
        elif choix == "6":
            reserves_argent(nom_fichier)
        elif choix =='7':
            charger_donnees_mois(nom_fichier)
        elif choix == '8':
            afficher_totals(nom_fichier)
        else:
            print("Option non valide. Veuillez choisir une option valide (1-5) ou 0 pour quitter.")



def main():
    print("Bonjour et Bienvenue à toi\n")
    
    mois_valides = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
    
    while True:
        nom_fichier = input("Entrez le nom du mois en minuscule et sans accents ni ponctuation : ").strip().lower()
        
        if nom_fichier in mois_valides:
            break
        else:
            print("Mois invalide. Veuillez entrer un mois valide.")

    lire_donnees_texte(nom_fichier)
    menu(nom_fichier)
    
    #test


if __name__ == "__main__":
    main()
