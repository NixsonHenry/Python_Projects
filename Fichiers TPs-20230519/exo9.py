import sqlite3

class Personne:
    def __init__(self, nom, prenom, age, ville):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.ville = ville

class Database:
    def __init__(self, db_name):
        self.connexion = sqlite3.connect(db_name)
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personnes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prenom TEXT,
                age INTEGER,
                ville TEXT
            )
        ''')
        self.connexion.commit()

    def ajouter_personne(self, personne):
        self.cursor.execute('''
            INSERT INTO personnes (nom, prenom, age, ville)
            VALUES (?, ?, ?, ?)
        ''', (personne.nom, personne.prenom, personne.age, personne.ville))
        self.connexion.commit()

    def recuperer_personnes(self):
        self.cursor.execute('''
            SELECT nom, prenom, age, ville FROM personnes
        ''')
        rows = self.cursor.fetchall()
        personnes = []
        for row in rows:
            personne = Personne(row[0], row[1], row[2], row[3])
            personnes.append(personne)
        return personnes

    def fermer_connexion(self):
        self.connexion.close()

db = Database('moun.db')

while True:
    choix = input("Voulez-vous lire, écrire ou quitter le programme ? (l/e/q) ")

    if choix == 'e':
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prénom : ")
        age = int(input("Entrez votre âge : "))
        ville = input("Entrez votre ville : ")
        personne = Personne(nom, prenom, age, ville)
        db.ajouter_personne(personne)
        print("Les informations ont été sauvegardées avec succès dans la base de données 'personnes.db'.")

    elif choix == 'l':
        personnes = db.recuperer_personnes()
        for personne in personnes:
            print("Nom = ", personne.nom)
            print("Prénom = ", personne.prenom)
            print("Âge = ", personne.age)
            print("Ville = ", personne.ville)
            print("--------------------")
        print("Les informations ont été récupérées avec succès depuis la base de données 'personnes.db'.")

    elif choix == 'q':
        db.fermer_connexion()
        break

    else:
        print("Erreur : choix incorrect. Veuillez entrer 'l' pour lire, 'e' pour écrire ou 'q' pour quitter le programme.")

print("Fin du programme.")
