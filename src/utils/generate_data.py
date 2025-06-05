import random
from typing import List
from src.models.classroom import Classroom
from src.models.matter import Matter
from src.models.people import People
from src.models.rating import Rating


def generate_school_dataset():
    """
    Génère un jeu de données complet pour le système scolaire
    avec au minimum 30 éléments par classe
    """

    # === CRÉATION DES CLASSES ===
    classrooms = [
        Classroom("6A", "6ème"),
        Classroom("6B", "6ème"),
        Classroom("5A", "5ème"),
        Classroom("5B", "5ème"),
        Classroom("4A", "4ème"),
        Classroom("4B", "4ème"),
        Classroom("3A", "3ème"),
        Classroom("3B", "3ème"),
        Classroom("2A", "2nde"),
        Classroom("2B", "2nde"),
        Classroom("1A", "1ère"),
        Classroom("1B", "1ère"),
        Classroom("TA", "Terminale"),
        Classroom("TB", "Terminale"),
    ]

    # === CRÉATION DES MATIÈRES ===
    matters = [
        Matter("Mathématiques"),
        Matter("Français"),
        Matter("Histoire-Géographie"),
        Matter("Sciences Physiques"),
        Matter("Sciences de la Vie et de la Terre"),
        Matter("Anglais"),
        Matter("Espagnol"),
        Matter("Arts Plastiques"),
        Matter("Éducation Physique et Sportive"),
        Matter("Technologie"),
        Matter("Musique"),
        Matter("Philosophie"),
        Matter("Économie"),
        Matter("Informatique"),
        Matter("Chimie"),
        Matter("Physique"),
        Matter("Littérature"),
        Matter("Latin"),
        Matter("Allemand"),
        Matter("Italien"),
        Matter("Biologie"),
        Matter("Géologie"),
        Matter("Sociologie"),
        Matter("Psychologie"),
        Matter("Droit"),
        Matter("Comptabilité"),
        Matter("Marketing"),
        Matter("Communication"),
        Matter("Design"),
        Matter("Architecture"),
        Matter("Ingénierie"),
        Matter("Médecine"),
    ]

    # === LISTES DE PRÉNOMS FRANÇAIS ===
    prenoms_garcons = [
        "Louis", "Gabriel", "Raphaël", "Arthur", "Lucas", "Jules", "Adam", "Maël", "Paul", "Hugo",
        "Ethan", "Gabin", "Aaron", "Mohamed", "Léo", "Tom", "Nathan", "Théo", "Noah", "Liam",
        "Mathis", "Léon", "Noa", "Timéo", "Maxime", "Antoine", "Clément", "Baptiste", "Pierre",
        "Alexandre", "Martin", "Romain", "Thomas", "Nicolas", "Julien", "David", "Benjamin",
        "Samuel", "Victor", "Alexis", "Valentin", "Simon", "Olivier", "Maxence", "Bastien"
    ]

    prenoms_filles = [
        "Jade", "Louise", "Emma", "Ambre", "Alice", "Rose", "Anna", "Romy", "Mia", "Lina",
        "Juliette", "Chloé", "Léa", "Manon", "Mathilde", "Agathe", "Adèle", "Mila", "Julia",
        "Zoé", "Camille", "Eva", "Inès", "Romane", "Iris", "Victoire", "Elena", "Célia",
        "Marie", "Sarah", "Clara", "Anaïs", "Pauline", "Océane", "Laura", "Julie", "Margot",
        "Charlotte", "Élise", "Léana", "Luna", "Nora", "Lola", "Capucine", "Maëlys"
    ]

    noms_famille = [
        "Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau",
        "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel",
        "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent",
        "Muller", "Lefevre", "Faure", "Andre", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier",
        "Chevalier", "Francois", "Legrand", "Gauthier", "Garcia", "Perrin", "Robin", "Clement",
        "Morin", "Nicolas", "Henry", "Roussel", "Matthieu", "Gautier", "Masson", "Marchand"
    ]

    # === GÉNÉRATION DES ÉLÈVES (30+ par classe) ===
    all_people = []
    for classroom in classrooms:
        # Générer entre 30 et 35 élèves par classe
        num_students = random.randint(30, 35)

        for i in range(num_students):
            # Choix aléatoire du genre et du prénom correspondant
            is_male = random.choice([True, False])
            if is_male:
                prenom = random.choice(prenoms_garcons)
            else:
                prenom = random.choice(prenoms_filles)

            nom = random.choice(noms_famille)
            nom_complet = f"{prenom} {nom}"

            # Âge approprié selon le niveau
            age_ranges = {
                "6ème": (11, 12),
                "5ème": (12, 13),
                "4ème": (13, 14),
                "3ème": (14, 15),
                "2nde": (15, 16),
                "1ère": (16, 17),
                "Terminale": (17, 18)
            }
            min_age, max_age = age_ranges[classroom.grade]
            age = random.randint(min_age, max_age)

            # Créer l'élève (sans les notes pour l'instant)
            student = People(classroom, nom_complet, age, [])
            all_people.append(student)

    # === GÉNÉRATION DES NOTES ===
    all_ratings = []

    # Matières par niveau scolaire
    subjects_by_grade = {
        "6ème": ["Mathématiques", "Français", "Histoire-Géographie", "Sciences de la Vie et de la Terre",
                 "Anglais", "Arts Plastiques", "Éducation Physique et Sportive", "Technologie", "Musique"],
        "5ème": ["Mathématiques", "Français", "Histoire-Géographie", "Sciences Physiques",
                 "Sciences de la Vie et de la Terre",
                 "Anglais", "Espagnol", "Arts Plastiques", "Éducation Physique et Sportive", "Technologie", "Musique"],
        "4ème": ["Mathématiques", "Français", "Histoire-Géographie", "Sciences Physiques",
                 "Sciences de la Vie et de la Terre",
                 "Anglais", "Espagnol", "Arts Plastiques", "Éducation Physique et Sportive", "Technologie", "Latin"],
        "3ème": ["Mathématiques", "Français", "Histoire-Géographie", "Sciences Physiques",
                 "Sciences de la Vie et de la Terre",
                 "Anglais", "Espagnol", "Arts Plastiques", "Éducation Physique et Sportive", "Technologie", "Latin"],
        "2nde": ["Mathématiques", "Français", "Histoire-Géographie", "Sciences Physiques",
                 "Sciences de la Vie et de la Terre",
                 "Anglais", "Espagnol", "Éducation Physique et Sportive", "Économie", "Littérature"],
        "1ère": ["Mathématiques", "Français", "Histoire-Géographie", "Physique", "Chimie", "Biologie",
                 "Anglais", "Philosophie", "Économie", "Littérature", "Informatique"],
        "Terminale": ["Mathématiques", "Français", "Histoire-Géographie", "Physique", "Chimie", "Biologie",
                      "Anglais", "Philosophie", "Économie", "Littérature", "Informatique", "Droit"]
    }

    # Commentaires types pour les notes
    comments = [
        "Excellent travail, continuez ainsi !",
        "Très bon résultat, bravo !",
        "Bon travail dans l'ensemble",
        "Résultat satisfaisant",
        "Peut mieux faire, des efforts à fournir",
        "Travail insuffisant, il faut se ressaisir",
        "Résultat décevant, voir les parents",
        "Très belle progression !",
        "Élève sérieux et appliqué",
        "Manque de rigueur dans le travail",
        "Participation active en classe",
        "Élève discret mais efficace",
        "Besoins d'aide supplémentaire",
        "Potentiel non exploité",
        "Remarquable !",
        "Pas de commentaire particulier"
    ]

    # Générer les notes pour chaque élève
    for person in all_people:
        grade_level = person.getClassroom().grade
        available_subjects = subjects_by_grade[grade_level]

        # Chaque élève a des notes dans toutes les matières de son niveau
        for subject_name in available_subjects:
            # Trouver l'objet Matter correspondant
            subject_matter = next((m for m in matters if m.getName() == subject_name), None)
            if subject_matter:
                # Générer entre 3 et 8 notes par matière
                num_ratings = random.randint(3, 8)

                for _ in range(num_ratings):
                    # Génération d'une note réaliste (distribution normale centrée sur 12)
                    base_score = random.gauss(12, 3)
                    # Contraindre entre 0 et 20
                    score = max(0, min(20, round(base_score * 2) / 2))  # Arrondi au demi-point

                    # Choisir un commentaire approprié selon la note
                    if score >= 16:
                        comment = random.choice(comments[:4])
                    elif score >= 12:
                        comment = random.choice(comments[4:8])
                    elif score >= 8:
                        comment = random.choice(comments[8:12])
                    else:
                        comment = random.choice(comments[12:])

                    # Créer la note
                    rating = Rating(person, subject_matter, score, comment)
                    all_ratings.append(rating)

                    # Ajouter la note à l'élève
                    if person.ratings is None:
                        person.ratings = []
                    person.ratings.append(rating)

    return {
        'classrooms': classrooms,
        'matters': matters,
        'people': all_people,
        'ratings': all_ratings
    }


def display_statistics(dataset):
    """
    Affiche des statistiques sur le jeu de données généré
    """
    print("=== STATISTIQUES DU JEU DE DONNÉES ===")
    print(f"Nombre de classes: {len(dataset['classrooms'])}")
    print(f"Nombre de matières: {len(dataset['matters'])}")
    print(f"Nombre total d'élèves: {len(dataset['people'])}")
    print(f"Nombre total de notes: {len(dataset['ratings'])}")

    print("\n=== RÉPARTITION PAR CLASSE ===")
    for classroom in dataset['classrooms']:
        students_in_class = [p for p in dataset['people'] if p.getClassroom().name == classroom.name]
        print(f"{classroom.name} ({classroom.grade}): {len(students_in_class)} élèves")

    print("\n=== EXEMPLES D'ÉLÈVES ===")
    for i, person in enumerate(dataset['people'][:5]):  # Afficher les 5 premiers
        num_ratings = len(person.ratings) if person.ratings else 0
        print(f"{person.name} - {person.getClassroom().name} - {person.age} ans - {num_ratings} notes")


def save_dataset_example(dataset):
    """
    Exemple d'utilisation du jeu de données
    """
    print("\n=== EXEMPLE D'UTILISATION ===")

    # Exemple 1: Trouver tous les élèves d'une classe
    classe_6a = next(c for c in dataset['classrooms'] if c.name == "6A")
    eleves_6a = [p for p in dataset['people'] if p.getClassroom().name == classe_6a.name]
    print(f"Élèves de la classe 6A: {len(eleves_6a)}")

    # Exemple 2: Calculer la moyenne d'un élève en mathématiques
    math_matter = next(m for m in dataset['matters'] if m.getName() == "Mathématiques")
    premier_eleve = eleves_6a[0]
    math_ratings = [r for r in premier_eleve.ratings if r.getMatter().getName() == "Mathématiques"]
    if math_ratings:
        moyenne = sum(r.getValue() for r in math_ratings) / len(math_ratings)
        print(f"Moyenne de {premier_eleve.name} en Mathématiques: {moyenne:.2f}/20")

    # Exemple 3: Statistiques générales
    all_scores = [r.getValue() for r in dataset['ratings']]
    moyenne_generale = sum(all_scores) / len(all_scores)
    print(f"Moyenne générale de l'établissement: {moyenne_generale:.2f}/20")


# === EXÉCUTION ===
if __name__ == "__main__":
    print("Génération du jeu de données scolaire...")
    dataset = generate_school_dataset()

    display_statistics(dataset)
    save_dataset_example(dataset)

    print("\n=== JEU DE DONNÉES GÉNÉRÉ AVEC SUCCÈS ===")
    print("Vous pouvez maintenant utiliser les variables:")
    print("- dataset['classrooms']: Liste des classes")
    print("- dataset['matters']: Liste des matières")
    print("- dataset['people']: Liste des élèves")
    print("- dataset['ratings']: Liste des notes")