# Étape 1 : Créer un dictionnaire Python appelé `personne`
personne = {'nom': '', 'prenom': '', 'age': '', 'ville': ''}

# Étape 2 : Demander à l'utilisateur de saisir les valeurs pour chaque clé du dictionnaire `personne`
personne['nom'] = input("Entrez votre nom : ")
personne['prenom'] = input("Entrez votre prénom : ")
personne['age'] = input("Entrez votre âge : ")
personne['ville'] = input("Entrez votre ville : ")

# Étape 3 : Créer un fichier texte appelé `'personne.txt'`
import os
os.chdir('C:/Users/xondy/OneDrive/Bureau/IBM SPSS Statistics 26.0 IF006 + Crack [www.TheWindowsForum.com]/Python Avancé/Fichiers TPs-20230519/exo1.py')
fichier = open('personne.txt', 'w')

# Étape 4 : Écrire les informations stockées dans le dictionnaire `personne` dans le fichier `'personne.txt'`
fichier.write(f"nom: {personne['nom']}\n")
fichier.write(f"prenom: {personne['prenom']}\n")
fichier.write(f"age: {personne['age']}\n")
fichier.write(f"ville: {personne['ville']}\n")

# Étape 5 : Afficher un message à l'utilisateur pour lui indiquer que les informations ont été sauvegardées avec succès dans le fichier `'personne.txt'`
print("Les informations ont été sauvegardées avec succès dans le fichier 'personne.txt'.")

# Fermer le fichier
fichier.close()


