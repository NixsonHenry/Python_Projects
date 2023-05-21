import sqlite3

# Connexion à la base de données
connexion = sqlite3.connect('personnes.db')

# Création de la table
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

# Fermeture de la connexion à la base de données
connexion.close()
