import datetime
import json

argent_net = 0
complement_revenu = 0
prime = 0
depenses = 0
argent_disponible = 0
prelevements_globaux = []


def enregistrer_donnees_texte():
    global salaire,prime,prelevements_globaux, argent_net, depenses_possibles,complement_revenu,depenses,argent_disponible,reserves
    donnees = {
        "salaire": salaire,
        "prelevements_globaux": prelevements_globaux,
        "argent_net": argent_net,
        "depenses_possibles": depenses_possibles,
        "prime": prime,
        "complement_revenu": complement_revenu,
        "depenses":depenses,
        "argent_disponible" : argent_disponible,
        "reserves" : reserves
    }
    with open("donnees.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)  



def lire_donnees_texte():
    global salaire, prelevements_globaux, argent_net, depenses_possibles, prime, complement_revenu, depenses,argent_disponible,reserves
    try:
        with open("donnees.json", "r") as fichier:
            donnees = json.load(fichier)
            salaire = donnees.get("salaire", 0)
            prelevements_globaux = donnees.get("prelevements_globaux", [])
            argent_net = donnees.get("argent_net", 0)
            depenses_possibles = donnees.get("depenses_possibles", 0)
            prime = donnees.get("prime", 0)
            complement_revenu = donnees.get("complement_revenu", 0)
            depenses = donnees.get("depenses", 0)
            argent_disponible = donnees.get("argent_disponible", 0)
            reserves = donnees.get("reserves",0)
    except FileNotFoundError:
        print("Fichier de données introuvable. Création d'un nouveau fichier.")
        # Initialiser toutes les variables à des valeurs par défaut
        salaire = 0
        prelevements_globaux = []
        argent_net = 0
        depenses_possibles = 0
        prime = 0
        complement_revenu = 0
        depenses = 0
        argent_disponible = 0
        reserves = 0
        enregistrer_donnees_texte()  # Appelle la fonction pour créer le fichier avec les valeurs par défaut
    except json.JSONDecodeError:
        print("Erreur lors de la lecture des données. Format de fichier incorrect.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")



def menu_salaire():
    while True:
        print("\nMenu Salaire\n")
        print("1. Entrer le salaire reçu")
        print("2. Entrer une prime reçue")
        print("3. Entrer un complément au salaire")
        print("4. Corriger une erreur")
        print("5. Quitter\n")
        try:
            # Utiliser directement calculer_argent_disponible() dans le print peut lever une exception si mal configuré
            argent_dispo = calculer_argent_disponible()  
            print(f"Vous avez {argent_dispo} € de disponible")
        except Exception as e:
            print(f"Une erreur est survenue lors du calcul de l'argent disponible: {e}")
            # Option de gestion d'erreur, par exemple, continuer ou quitter
            continue

        try:
            choix = int(input("Choisissez une catégorie : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choix == 1:
            salaire_reçu()
        elif choix == 2:
            prime_reçue()
        elif choix == 3:
            complement()
        elif choix == 4:
            corriger_erreur()
        elif choix == 5:
            print("Quitter le menu Salaire.")
            break
        else:
            print("Option non valide, veuillez choisir un numéro entre 1 et 5.")



def salaire_reçu():
    global salaire
    global argent_net
    while True:
        try:
            salaire_input = input("Combien avez-vous reçu ? :")
            salaire_temp = float(salaire_input)  # Tente de convertir l'entrée en float
            if salaire_temp < 0:
                print("Le montant du salaire ne peut pas être négatif. Veuillez entrer un montant valide.")
                continue
            salaire = salaire_temp
            break  # Sortie de la boucle si la conversion est réussie et le salaire est positif
        except ValueError:
            print("Veuillez entrer un nombre valide. Par exemple, 2500.50")
            # La boucle continue, demandant à l'utilisateur de réessayer

    print("Prise en compte de votre salaire...")
    argent_net += salaire  # Met à jour argent_net avec le nouveau salaire

    enregistrer_donnees_texte()  # Sauvegarde les données après la mise à jour


def prime_reçue():
    global prime
    global argent_net

    while True:
        try:
            prime_input = input("Combien avez-vous reçu en prime ? :")
            prime_temp = float(prime_input)  # Essaie de convertir l'entrée en float
            if prime_temp < 0:
                print("Le montant de la prime ne peut pas être négatif. Veuillez entrer un montant valide.")
                continue
            prime = prime_temp
            break  # Sortie de la boucle si la conversion est réussie et la prime est positive
        except ValueError:
            print("Veuillez entrer un nombre valide. Par exemple, 500.00")
            # La boucle continue, demandant à l'utilisateur de réessayer

    print("Prise en compte de votre prime...")
    argent_net += prime  # Met à jour argent_net avec la nouvelle prime

    enregistrer_donnees_texte()  # Sauvegarde les données après la mise à jour

def complement():
    global argent_net
    global complement_revenu

    while True:
        try:
            complement_input = input("Combien avez-vous eu en complément ? :")
            complement_temp = float(complement_input)  # Essaie de convertir l'entrée en float
            if complement_temp < 0:
                print("Le montant du complément ne peut pas être négatif. Veuillez entrer un montant valide.")
                continue
            complement_revenu = complement_temp
            break  # Sortie de la boucle si la conversion est réussie et le complément est positif
        except ValueError:
            print("Veuillez entrer un nombre valide. Par exemple, 300.00")
            # La boucle continue, demandant à l'utilisateur de réessayer

    print("Prise en compte de votre complément...")
    argent_net += complement_revenu  # Met à jour argent_net avec le nouveau complément

    enregistrer_donnees_texte()  # Sauvegarde les données après la mise à jour



def corriger_erreur():
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
                break  # Sortie de la boucle si l'entrée est valide
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    argent_net -= erreur  # Applique la correction
    print(f"Vous avez donc {calculer_argent_disponible()} € disponible après cette correction.")

    enregistrer_donnees_texte()



def menu_prelevements():
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
                ajouter_prelevements()
            elif choix == 2:
                nom_prelevement = input("Entrez le nom exact du prélèvement que vous voulez supprimer ou entrez 'q' pour quitter : ")
                if nom_prelevement.lower() == "q":
                    print("Retour au menu principal...")
                else:
                    supprimer_prelevement(nom_prelevement)
            elif choix == 3:
                afficher_prelevements()
            elif choix == 4:
                print("Retour au menu principal...")
                break
            else:
                print("Option non valide. Veuillez choisir un nombre entre 1 et 4.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre. Veuillez réessayer.")






def ajouter_prelevements():
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
                continue  # Redémarre la boucle pour permettre une nouvelle entrée
                
            prelevements_globaux.append({'nom': nom, 'montant': montant})
            print(f"Prélèvement '{nom}' de {montant} € ajouté avec succès.")
            enregistrer_donnees_texte()
            break
        
        except ValueError:
            print("Veuillez entrer un montant valide (nombre). Réessayez.")





def supprimer_prelevement(nom_prelevement):
    global prelevements_globaux
    prelevements_avant = prelevements_globaux.copy()  # Crée une copie de la liste actuelle

    # Utilise une liste en compréhension pour supprimer le prélèvement avec le nom spécifié
    prelevements_globaux = [prelevement for prelevement in prelevements_globaux if prelevement['nom'] != nom_prelevement.lower()]

    # Vérifie si des prélèvements ont été supprimés
    if len(prelevements_avant) == len(prelevements_globaux):
        print(f"Aucun prélèvement avec le nom '{nom_prelevement}' trouvé.")
    else:
        print(f"Prélèvement '{nom_prelevement}' supprimé si existant.")
        enregistrer_donnees_texte()


def afficher_prelevements():
    if prelevements_globaux:
        print("\nListe des prélèvements :")
        for prelevement in prelevements_globaux:
            print(f"Nom: {prelevement['nom'].capitalize()}, Montant: {prelevement['montant']} €")
    else:
        print("\nAucun prélèvement n'a été ajouté.")

    input("\nAppuyez sur Entrée pour continuer...")


    



def calcul_depenses():
    global argent_net, prelevements_globaux  # Pas besoin de 'argent_disponible' comme variable globale
    
    while True:
        argent_disponible = calculer_argent_disponible()  # Calculez dynamiquement
        print(f"Vous avez {argent_disponible} € de disponible.")
        depense_input = input("Combien as-tu dépensé ? (Appuyez sur 'q' pour quitter) : ")
        
        if depense_input.lower() == "q":  
            break  

        try:
            depense = float(depense_input)
            if depense <= argent_disponible:  # Vérifiez si la dépense est possible
                argent_net -= depense  # Appliquez la dépense
                print(f"Après dépense, vous avez {calculer_argent_disponible()} € de disponible.")
                enregistrer_donnees_texte()
            else:
                print("Dépense refusée. Vous n'avez pas assez d'argent disponible.")
        except ValueError:  
            print("Entrez une valeur valide ou 'q' pour quitter.")




def remise_a_zero():
    global salaire, prime, argent_net, depenses_possibles, prelevements_globaux, complement_revenu

    salaire = 0
    argent_net = 0
    depenses_possibles = 0
    prelevements_globaux = []
    complement_revenu = 0

    print("Données réinitialisées. Bienvenue dans votre nouveau mois, ne dépensez pas trop :)")

    enregistrer_donnees_texte()


def calculer_argent_disponible():
    global argent_net, prelevements_globaux
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

def reserves_argent():
    global reserves
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
                reserves += reserves_input
                print(f"Votre nouveau solde est de {reserves} €.")
            except ValueError:
                print("Erreur : Veuillez entrer un montant valide.")
        elif action == '2':
            try:
                retrait = float(input("Combien d'argent voulez-vous retirer : "))
                if retrait <= reserves:
                    reserves -= retrait
                    print(f"Vous avez retiré {retrait} €. Votre nouveau solde est de {reserves} €.")
                else:
                    print("Vous n'avez pas suffisamment d'argent en réserve.")
            except ValueError:
                print("Erreur : Veuillez entrer un montant valide.")
        else:
            print("Option non valide. Veuillez choisir une option valide.")




def menu():
    while True:
        print("\nMenu Principal\n")
        print("Options :")
        print("1. Gérer les entrées d'argent")
        print("2. Gérer les prélèvements")
        print("3. Calculer des prévisions d'économies")
        print("4. Ajouter ou supprimer une dépense")
        print("5. Commencer un nouveau mois / Remise à zéro")
        print("6. Ajouter / Supprimer de l'argent de côté")
        print("0. Quitter le programme\n")

        argent_dispo = calculer_argent_disponible()  
        print(f"Vous avez {argent_dispo} € de disponible")

        choix = input("Sélectionnez une option en entrant le numéro correspondant : ")
        
        if choix == "0":
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break
        elif choix == "1":
            menu_salaire()
        elif choix == "2":
            menu_prelevements()
        elif choix == "3":
            calcul_objectif_argent()
        elif choix == "4":
            calcul_depenses()
        elif choix == "5":
            remise_a_zero()
        elif choix == "6":
            reserves_argent()
        else:
            print("Option non valide. Veuillez choisir une option valide (1-5) ou 0 pour quitter.")



def main():
    print("Bonjour et Bienvenue à toi\n")
    lire_donnees_texte()
    menu()

if __name__ == "__main__":
    main()

