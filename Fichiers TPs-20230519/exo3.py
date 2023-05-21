import csv

# Créer une liste de dictionnaires Python
personnes = [
    {'nom': 'Dupont', 'prenom': 'Pierre', 'age': 30, 'ville': 'Paris'},
    {'nom': 'Martin', 'prenom': 'Sophie', 'age': 25, 'ville': 'Lyon'},
    {'nom': 'Durand', 'prenom': 'Jean', 'age': 40, 'ville': 'Marseille'}
]

# Sauvegarder les dictionnaires dans un fichier CSV
with open('personnes_.csv', 'w', newline='') as fichier:
    writer = csv.DictWriter(fichier, fieldnames=['nom', 'prenom', 'age', 'ville'])
    writer.writeheader()
    for personne in personnes:
        writer.writerow(personne)
import csv
# Lire les informations depuis le fichier CSV
with open('personnes.csv', 'r') as fichier:
    reader = csv.DictReader(fichier)
    for row in reader:
        print(row)