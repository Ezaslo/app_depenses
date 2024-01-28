import datetime
import json

argent_net = 0
complement_revenu = 0
prime = 0
depenses = 0
argent_disponible = 0
prelevements_globaux = []

def enregistrer_donnees_texte():
    global salaire,prime,prelevements_globaux, argent_net, depenses_possibles,complement_revenu,depenses,argent_disponible
    donnees = {
        "salaire": salaire,
        "prelevements_globaux": prelevements_globaux,
        "argent_net": argent_net,
        "depenses_possibles": depenses_possibles,
        "prime": prime,
        "complement_revenu": complement_revenu,
        "depenses":depenses,
        "argent_disponible" : argent_disponible
    }
    with open("donnees.json", "w") as fichier:
        json.dump(donnees, fichier, indent=4)  



def lire_donnees_texte():
    global salaire, prelevements_globaux, argent_net, depenses_possibles, prime, complement_revenu, depenses,argent_disponible
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
    salaire =float(input("Combien avez-vous reçu ? :"))
    print("prise en compte de votre salaire...")
    argent_net = argent_net + salaire

    enregistrer_donnees_texte()

def prime_reçue():
    global prime
    global argent_net
    
    prime =float(input("Combien avez-vous reçu ? :"))
    print("prise en compte de votre prime...")
    argent_net = argent_net + prime
    
    enregistrer_donnees_texte()

def complement():
    
    global argent_net
    global complement_revenu
    
    complement_revenu = float(input("Combien avez-vous eu en complement? :"))
    print("prise en compte de votre complement..")
    argent_net = argent_net + complement_revenu
    
    enregistrer_donnees_texte()


def corriger_erreur():
    global argent_net
    erreur = float(input("Combien voulez vous enlever à votre argent disponible : "))

    argent_net = argent_net - erreur
    print(f"vous avez donc {argent_net} € de disponilbe")
    
    enregistrer_donnees_texte()


def menu_prelevements():
    
    
    
    while True:
        print("Menu des prelevements\n")

        print("1. AJouter un prélèvement")
        print("2. Supprimer un prélèvement")
        print("3. Voir les prélèvement")
        print("4. Retour au menu principal")
        choix = (input(""))
        try : 
            choix =int(choix)

            if choix == 1:
                ajouter_prelevements()
        

            elif choix == 2:
                nom_prelevement = input("Entrez le nom exact du prélèvement ue vous voulez supprimer ou entrez 'q' pour quitter : ")
                if nom_prelevement == "q":
                    print("Retour au menu...")
                else:
                    supprimer_prelevement(nom_prelevement)

            elif choix == 3:
                afficher_prelevements()
            
            elif choix == 4:
                break

            else :
                print("Erreur : Vous devez choisir un nombre entre 1 et 4 ")
        except ValueError: 
            print("Erreur : Vous devez entrer un chiffre")





def ajouter_prelevements():
    while True: 
        nom = input("Entrez le nom du prélèvement, appuyez sur 'q' pour quitter: ").lower()
        if nom == "q":
            
            enregistrer_donnees_texte()

            break
        montant = input("Entrez le montant du prélèvement, appuyez sur 'q' pour quitter: ").lower()
        if montant == "q":
            
            enregistrer_donnees_texte()
            break
        try:
            montant = float(montant)  # Assurez-vous que le montant est un nombre
            prelevements_globaux.append({'nom': nom, 'montant': montant})
            
            enregistrer_donnees_texte()
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour le montant.")
            
            enregistrer_donnees_texte()





def supprimer_prelevement(nom_prelevement):
    global prelevements_globaux
    prelevements_globaux = [prelevement for prelevement in prelevements_globaux if prelevement['nom'] != nom_prelevement.lower()]

    print(f"Prélèvement '{nom_prelevement}' supprimé si existant.")

    enregistrer_donnees_texte()

def afficher_prelevements():
    if prelevements_globaux:
        print("\nListe des prélèvements :")
        for prelevement in prelevements_globaux:
            print(f"Nom: {prelevement['nom'].capitalize()}, Montant: {prelevement['montant']} €")
    else:
        print("\nAucun prélèvement n'a été ajouté.")

    while True :
            try :  
                reponse = input("\nAppuyez sur 'q' pour quitter : ").lower()
                if reponse == "q":
                    break
            except : 
                print("")    
    
    enregistrer_donnees_texte()
    return  


    



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
    global salaire,prime,prelevements_globaux, argent_net, depenses_possibles,complement_revenu,prelevements

    salaire = 0
    prelevements = 0
    argent_net = 0
    depenses_possibles = 0
    prelevements_globaux = []
    complement_revenu = 0

    print("Données réinitialisés bienvenue dans votre nouveau mois, ne depensez pas trop :)")
    
    enregistrer_donnees_texte()

def calculer_argent_disponible():
    global argent_net, prelevements_globaux
    total_prelevements = sum(prelevement['montant'] for prelevement in prelevements_globaux)
    argent_disponible = argent_net - total_prelevements
    return argent_disponible





import datetime

def calcul_objectif_argent():
    global depenses_possibles

    
    
    while True:
                reserves = float(input("Combien avez vous déjà mis d'argent de coté ? "))
                enregistrer_donnees_texte()
                
                try:
                    objectif = float(input("Combien d'argent souhaitez-vous mettre de côté en tout ? "))
                    if objectif < 0:
                        raise ValueError("L'objectif d'économie ne peut pas être négatif.")

                    annee_estimation = int(input("Jusqu'à quelle année souhaitez-vous estimer vos économies ? "))
                    now = datetime.datetime.now()
                    if annee_estimation <= now.year:
                        raise ValueError("L'année d'estimation doit être dans le futur.")

                    mois_restants = (annee_estimation - now.year) * 12
                    if mois_restants <= 0:
                        raise ValueError("Nombre de mois restants invalide.")
                    
                    objectif2 = objectif - reserves
                    montant_mensuel = objectif2 / mois_restants
                    argent_mis_de_cote = montant_mensuel * mois_restants


                    print(f"Si vous mettez de coté {montant_mensuel:.2f} € par mois, vous aurez environ {argent_mis_de_cote:.2f} € d'économies jusqu'à l'année {annee_estimation} ce qui vous permettra d'attendeindre votre objectif de {objectif} €.")
                    break
                except ValueError as ve:
                    print(f"Erreur : {ve}")
                except Exception as e:
                    print(f"Une erreur inattendue est survenue : {e}")

def menu():
    while True:
        print("\nMenu Principal\n")


        print("1. Entrées d'argent")
        print("2. Prélèvements")
        print("3. Faire des prevision sur les economies")
        print("4. Ajouter / Supprimer une depense")
        print("5. Commencer un nouveau mois / Remise à zero")

        

    
        choix =float(input(""))
        try: 
            if choix == 1:
                menu_salaire()
                
            elif choix == 2:
                menu_prelevements()
                
            elif choix == 3:
                calcul_objectif_argent()
            elif choix == 4:
                
                calcul_depenses()

            
            elif choix == 5:
                remise_a_zero()
        except ValueError:
                print("erreur entrez une donnée valide")


def main():
    print("Bonjour et Bienvenue à toi\n")
    lire_donnees_texte()
    menu()

if __name__ == "__main__":
    main()

