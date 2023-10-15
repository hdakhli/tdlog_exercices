"""
Une méthode agile est une approche itérative et collaborative pour
mener à bien un projet.
Elle génère un produit de haute qualité tout en prenant en compte
l’évolution des besoins des clients.

La méthode la plus connue est Scrum.

Au début d'un projet un « backlog », ensemble de tache à réaliser
est défini avec le client.
Ce « backlog » évolue dans le temps en fonction du besoin de client.
On peut y rajouter des taches comme on peut en enlever.

Durant le projet, une réunion avec l'équipe technique et l'équipe
opérationnelle est organisée à chaque
« sprint » (unité de temps composé de quelques semaines).
Lors cette réunion, le client valide ou non les taches
qui ont été réalisées durant la période de « sprint ».

Dans ce challenge, vous devez déterminer si à la date de la livraison
finale, le client obtient la totalité de son produit.


Format des données

Entrée
Ligne 1 : un entier N correspondant au nombre de sprints(réunion).
Ligne 2 : un entier T correspondant au nombre de taches dans le « backlog »
        initial.
Ligne 3 à N+2 : un entier V et un entier U séparés par un espace où V est
le nombre de taches validées
et U le nombre de taches à ajouter (si U est positif) ou à supprimer
(si U est négatif) dans le « backlog ».

Sortie
La chaîne OK si le backlog est vide. Sinon retourner la chaîne KO.

"""


def processLines(lines) -> str:
    # Lecture des entiers N et T à partir de la première ligne
    N = int(lines[0])
    T = int(lines[1])

    # Initialiser le nombre total de tâches
    total_tasks = T

    # Parcourir les lignes à partir de la troisième
    for i in range(2, N + 2):
        # Lire le nombre de tâches validées (V) et à ajouter ou supprimer (U)
        V, U = map(int, lines[i].split())

        # Mettre à jour le nombre total de tâches
        total_tasks += U

        # Vérifier si le nombre total de tâches est négatif (ce qui ne devrait pas arriver)
        if total_tasks < 0:
            return "KO"

        # Mettre à jour le nombre total de tâches après validation
        total_tasks -= V

    # Vérifier si le backlog est vide
    if total_tasks == 0:
        return "OK"
    else:
        return "KO"

# Exemple d'utilisation
lines = ['3', '5', '3 2', '2 -1', '1 0']
result = processLines(lines)
print(result)  # Cela devrait afficher "OK" dans cet exemple


