import json

# Créer un dictionnaire Python
personne = {'nom': 'Dupont', 'prenom': 'Pierre', 'age': 30, 'ville': 'Paris'}

# Sauvegarder le dictionnaire dans un fichier JSON
with open('personne02.json', 'w') as fichier:
    json.dump(personne, fichier)

# Lire les informations depuis le fichier JSON
with open('personne.json', 'r') as fichier:
    data = json.load(fichier)
    print(data)
