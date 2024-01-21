

def enregistrer_donnees_texte():
    with open("donnees.txt", "w") as fichier:
        fichier.write(f"Salaire: {salaire}\n")
        fichier.write(f"Prélèvements: {prelevements}\n")
        fichier.write(f"Argent Net: {argent_net}\n")
        fichier.write(f"Depenses Possibles: {depenses_possibles}\n")


def lire_donnees_texte():
    global salaire, prelevements, argent_net, depenses_possibles

    try:
        with open("donnees.txt", "r") as fichier:
            salaire = float(fichier.readline().split(": ")[1])
            prelevements = float(fichier.readline().split(": ")[1])
            argent_net = float(fichier.readline().split(": ")[1])
            depenses_possibles = float(fichier.readline().split(": ")[1])
    except FileNotFoundError:
        print("Fichier de données introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")


lire_donnees_texte()


def qsalaire_recu():
    global recu

    while True:
        try : 
            recu = input("As-tu reçu ton salaire ? (Oui/Non) : ").lower()
            if recu == "oui" or recu == "non":
                break
            else:
                print("Tu dois repondre par oui ou par non ")
        except Exception as e:
            print("Une erreur s'est produite :", e)

    return recu

    


def informations():
    global salaire
    global prelevements
    global argent_net
    global reponse

    salaire = float(input("Combien as-tu reçu ? "))
    
    prelevements = float(input("Quels sont tes prélèvements obligatoires ? "))
    
    autre_prelevements = {}
    
    while True:
        autre = input("Voulez-vous ajouter un autre prélèvement (Oui/Non) ? ").lower()
        
        if autre == "oui":
            nom_prelevement = input("Nom du prélèvement : ")
            montant_prelevement = float(input("Montant du prélèvement : "))
            autre_prelevements[nom_prelevement] = montant_prelevement
        elif autre == "non":
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
    
    total_prelevements = prelevements + sum(autre_prelevements.values())
    
    print(f"Okay, donc tu as reçu {salaire} € et on te prélève en tout {total_prelevements} € par mois ?")
    argent_net =  (salaire - total_prelevements)
    reponse = input("Oui/Non : ").lower()

    



def calcul_depenses():
    global depenses_possibles 
    global argent_net
    depenses_possibles = argent_net

    while depenses_possibles > 0:
        print(f"Tu as {depenses_possibles} € ")
        reponse = input("Combien as-tu dépensé ? (ou appuyez sur 'Q' pour quitter) : ")
        enregistrer_donnees_texte()

        if reponse.lower() == "q":
            print("Fermeture de l'application.")
            enregistrer_donnees_texte()
            exit()  

        depenses = float(reponse)
        depenses_possibles -= depenses
        argent_net = depenses_possibles
        enregistrer_donnees_texte()

        if depenses_possibles <= 0:
            print("Tu n'as plus d'argent")
            enregistrer_donnees_texte()


def remise_a_zero():
    salaire = 0
    prelevements = 0
    argent_net = 0
    depenses_possibles = 0

def main():
    print("Bonjour et Bienvenue à toi")

    while True:
        qsalaire_recu()
        if recu == "oui":
            informations()
        elif argent_net > 0:  
            print("D'accord, utilisons les informations que nous avons déjà.")
        else:
            print("Nous n'avons pas de données enregistrées. Veuillez saisir vos informations lorsque vous aurez reçu votre salaire.")

        if argent_net > 0:
            calcul_depenses()
        rep = input("voulez vous commencer un nouveau mois salarial ? ")
        if rep == "oui":
            remise_a_zero()
            print("valeurs remises à zero")
        else:
            print(" Au revoir ! ")
            break




main()
