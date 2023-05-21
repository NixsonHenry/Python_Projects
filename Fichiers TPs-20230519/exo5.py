import os

# Étape 1 : Demander à l'utilisateur s'il veut écrire ou lire dans le fichier
choix = input("Voulez-vous écrire ou lire dans le fichier ? (ecrire/lire) ")

if choix == "ecrire":
    # Étape 2 : Créer un dictionnaire Python appelé `personne`
    personne = {'nom': '', 'prenom': '', 'age': '', 'ville': ''}

    # Étape 3 : Demander à l'utilisateur de saisir les valeurs pour chaque clé du dictionnaire `personne`
    personne['nom'] = input("Entrez votre nom : ")
    personne['prenom'] = input("Entrez votre prénom : ")
    personne['age'] = input("Entrez votre âge : ")
    personne['ville'] = input("Entrez votre ville : ")

    # Étape 4 : Vérifier si le fichier existe
    if os.path.exists('personne.txt'):
        # Étape 5 : Demander à l'utilisateur s'il veut écraser le fichier existant ou ajouter les nouvelles informations à la suite
        ajout = input("Le fichier 'personne.txt' existe déjà. Voulez-vous écraser son contenu ou ajouter les nouvelles informations à la suite ? (ecraser/ajouter) ")

        if ajout == "ecraser":
            # Étape 6 : Créer un fichier texte appelé `'personne.txt'`
            fichier = open('personne.txt', 'w')
        elif ajout == "ajouter":
            # Étape 6 : Ouvrir le fichier texte appelé `'personne.txt'` en mode ajout
            fichier = open('personne.txt', 'a')
        else:
            # Si l'utilisateur a choisi une option invalide, afficher un message d'erreur et quitter le programme
            print("Option invalide. Veuillez choisir 'ecraser' ou 'ajouter'.")
            exit()
    else:
        # Étape 6 : Créer un fichier texte appelé `'personne.txt'`
        fichier = open('personne.txt', 'w')

    # Étape 7 : Écrire les informations stockées dans le dictionnaire `personne` dans le fichier `'personne.txt'`
    fichier.write(f"nom: {personne['nom']}\n")
    fichier.write(f"prenom: {personne['prenom']}\n")
    fichier.write(f"age: {personne['age']}\n")
    fichier.write(f"ville: {personne['ville']}\n\n")

    # Étape 8 : Afficher un message à l'utilisateur pour lui indiquer que les informations ont été sauvegardées avec succès dans le fichier `'personne.txt'`
    print("Les informations ont été sauvegardées avec succès dans le fichier 'personne.txt'.")
    
    # Fermer le fichier
    fichier.close()

elif choix == "lire":
    # Étape 2 : Vérifier si le fichier existe
    if os.path.exists('personne.txt'):
        # Étape 3 : Ouvrir le fichier texte appelé `'personne.txt'`
        fichier = open('personne.txt', 'r')

        # Étape 4 : Lire les informations stockées dans le fichier `'personne.txt'` et les afficher à l'utilisateur
        contenu = fichier.read()
        print(contenu)

        # Fermer le fichier
        fichier.close()
    else:
        # Si le fichier n'existe pas, afficher un message d'erreur
        print("Il n'y a aucun fichier 'personne.txt'.")
        
else:
    # Si l'utilisateur a choisi une option invalide, afficher un message d'erreur
    print("Option invalide. Veuillez choisir 'ecrire' ou 'lire'.")

