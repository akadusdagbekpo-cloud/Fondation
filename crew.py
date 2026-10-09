crew = [
    {
        "first_name": "Bel",
        "last_name": "Riose",
        "gender": "M",
        "age": 48,
        "role": "commandant",
    },
    {
        "first_name": "Gaal",
        "last_name": "Dornick",
        "gender": "F",
        "age": 34,
        "role": "technicien",
    },
    {
        "first_name": "Hugo",
        "last_name": "Crast",
        "gender": "M",
        "age": 37,
        "role": "pilote",
    },
    {
        "first_name": "Salvor",
        "last_name": "Hardin",
        "gender": "F",
        "age": 28,
        "role": "armurier",
    },
    {
        "first_name": "Novi",
        "last_name": "Sura",
        "gender": "F",
        "age": 25,
        "role": "entretien",
    },
]

ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]


def nom_deja_present(crew, nom):
    for member in crew:
        if nom.lower() == member["last_name"].lower():
            return True
    return False


def add_member(crew):
    while True:
        prenom = input("Prenom : ")
        if 3 <= len(prenom) <= 15:
            break
        print("Erreur : le prenom doit faire entre 3 et 15 caracteres.")

    while True:
        nom = input("Nom de famille : ")
        if 3 <= len(nom) <= 15:
            if not nom_deja_present(crew, nom):
                break
            print("Erreur : ce nom de famille existe deja dans l'equipage.")
        else:
            print("Erreur : le nom doit faire entre 3 et 15 caracteres.")

    while True:
        genre = input("Genre (F/M) : ")
        if genre.upper() == "F" or genre.upper() == "M":
            break
        print("Erreur : repondez F ou M.")

    while True:
        age_texte = input("Age : ")
        if age_texte.isdigit():
            age = int(age_texte)
            break
        print("Erreur : entrez un nombre entier.")

    while True:
        role = input("Role : ")
        if role.lower() in ROLES:
            break
        print(f"Erreur : entrez un role parmi {ROLES}.")

    member = {
        "first_name": prenom,
        "last_name": nom,
        "gender": genre.upper(),
        "age": age,
        "role": role.lower(),
    }

    crew.append(member)
    print(f"{prenom} {nom} ({genre} {age} ans, {role}) a ete ajoute(e) a l'equipage.")


def remove_member(crew):
    nom_a_retirer = input("Entrez le nom de famille du membre a retirer : ").strip()

    for member in crew:
        if member["last_name"].lower() == nom_a_retirer.lower():
            crew.remove(member)
            print(f"Le membre '{nom_a_retirer}' a ete retire de la liste avec succes.")
            break
    else:
        print(f"Aucun membre ne porte le nom '{nom_a_retirer}'.")


def display_crew(crew):
    if not crew:
        print("L'equipage est vide.")
        return

    print("=" * 30)
    print("EQUIPAGE".center(30, "="))
    print("=" * 30)

    for i, member in enumerate(crew):
        print(
            f"{i + 1}. {member['first_name']} {member['last_name']} "
            f"- {member['gender']}, {member['age']} ans - {member['role']}"
        )


def check_crew(crew):
    nb_members = len(crew)
    pilote = False
    technicien = False

    for member in crew:
        if member["role"].lower() == "pilote":
            pilote = True
        if member["role"].lower() == "technicien":
            technicien = True

    manques = []
    if nb_members < 2:
        manques.append("au moins 2 membres")
    if not pilote:
        manques.append("un pilote")
    if not technicien:
        manques.append("un technicien")

    if not manques:
        print("L'equipage est pret pour la mission !")
        return True
    else:
        print("Il manque : " + ", ".join(manques))
        return False


def ask_int(prompt):
    while True:
        texte = input(prompt)
        if texte.isdigit():
            return int(texte)
        print("Erreur : entrez un nombre entier.")


def find_member(crew, last_name):
    for member in crew:
        if member["last_name"].lower() == last_name.lower():
            return member
    return None