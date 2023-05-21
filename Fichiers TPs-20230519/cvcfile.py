import csv
donnees = [
    ["Nom", "Prénom", "Âge"],
    ["Dupont", "Jean", 28],
    ["Durand", "Marie", 42],
    ["Martin", "Luc", 36]
]
with open("mon_fichier01.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for ligne in donnees:
        writer.writerow(ligne)