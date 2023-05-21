import sqlite3

# Connexion à la base de données
connexion = sqlite3.connect('personnes.db')

# Demande à l'utilisateur s'il veut lire ou écrire dans la base de données
choix = input("Voulez-vous lire ou écrire dans la base de données ? (l/e) ")

if choix == 'e':
    # Création de la table s'il n'existe pas
    connexion.execute('''CREATE TABLE IF NOT EXISTS personnes
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nom TEXT,
                     prenom TEXT,
                     age INTEGER,
                     ville TEXT);''')

    # Demande des informations à l'utilisateur
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    age = int(input("Entrez votre âge : "))
    ville = input("Entrez votre ville : ")

    # Insertion des informations dans la base de données
    connexion.execute("INSERT INTO personnes (nom, prenom, age, ville) VALUES (?, ?, ?, ?)", (nom, prenom, age, ville))
    connexion.commit()

    # Affichage d'un message pour indiquer que les informations ont été sauvegardées
    print("Les informations ont été sauvegardées avec succès dans la base de données 'personnes.db'.")

elif choix == 'l':
    # Récupération des informations depuis la base de données
    cursor = connexion.execute("SELECT nom, prenom, age, ville FROM personnes")
    for row in cursor:
        print("Nom = ", row[0])
        print("Prénom = ", row[1])
        print("Âge = ", row[2])
        print("Ville = ", row[3])
        print("--------------------")

    # Affichage d'un message pour indiquer que les informations ont été récupérées
    print("Les informations ont été récupérées avec succès depuis la base de données 'personnes.db'.")

else:
    # Affichage d'un message d'erreur si l'utilisateur a entré une valeur incorrecte
    print("Erreur : choix incorrect. Veuillez entrer 'l' pour lire ou 'e' pour écrire dans la base de données.")

# Fermeture de la connexion à la base de données
connexion.close()
