# main.py
from fleet_data import GALACTICA_DATA
from crew import build_fleet
from storage import save_fleet, load_fleet
from spaceship import Spaceship
from person import Operator, Mentalist


def main():
    # Initialisation de la flotte avec les données par défaut
    current_fleet = build_fleet(GALACTICA_DATA)

    while True:
        print("\n===== Flotte Galactica - Poste de commandement =====")
        print("[1] Ajouter un membre")
        print("[2] Retirer un membre")
        print("[3] Afficher la flotte")
        print("[4] Vérifier un vaisseau")
        print("[5] Ajouter un vaisseau")
        print("[6] Statistiques de la flotte")
        print("[7] Sauvegarder la flotte")
        print("[8] Charger une flotte")
        print("[9] le nombre de vaisseau total")
        print("[0] Quitter")

        choice = input("Votre choix : ").strip()

        if choice == "0":
            print("Fermeture du programme. Bon vent, commandant !")
            break

        elif choice == "1":
            ship_name = input("Nom du vaisseau cible : ").strip()
            ship = current_fleet.find_spaceship(ship_name)
            if not ship:
                print(f"Erreur : Aucun vaisseau nommé « {ship_name} » n'a été trouvé.")
                continue
            try:
                m_type = (
                    input("Type de membre (Operator / Mentalist) : ")
                    .strip()
                    .capitalize()
                )
                first_name = input("Prénom : ").strip()
                last_name = input("Nom de famille : ").strip()
                gender = input("Genre (M/F) : ").strip().upper()
                age = int(input("Âge : ").strip())

                if m_type == "Operator":
                    role = input("Rôle : ").strip()
                    member = Operator(first_name, last_name, gender, age, role)
                elif m_type == "Mentalist":
                    member = Mentalist(first_name, last_name, gender, age)
                else:
                    print(
                        "Erreur : Type de membre inconnu (doit être Operator ou Mentalist)."
                    )
                    continue

                ship.add_member(member)
                print(f"Succès : {member.name} a été ajouté au vaisseau {ship.name}.")
            except ValueError as e:
                print(f"Erreur de validation : {e}")
            except Exception as e:
                print(f"Erreur inattendue : {e}")

        elif choice == "2":
            ship_name = input("Nom du vaisseau cible : ").strip()
            ship = current_fleet.find_spaceship(ship_name)
            if not ship:
                print(f"Erreur : Vaisseau introuvable.")
                continue
            member_name = input("Nom ou prénom du membre à retirer : ").strip()
            removed = ship.remove_member(member_name)
            if removed:
                print(f"Succès : {removed.name} a été retiré de {ship.name}.")
            else:
                print(
                    f"Erreur : Aucun membre portant ce nom n'a été trouvé dans ce vaisseau."
                )

        elif choice == "3":
            print(f"\n--- Flotte : {current_fleet.name} ---")
            if not current_fleet.spaceships:
                print("La flotte ne contient aucun vaisseau.")
            for ship in current_fleet.spaceships:
                print(f"\n> Vaisseau : {ship}")
                if not ship.crew:
                    print("  (Équipage vide)")
                for member in ship.crew:
                    print(f"  - {member}")

        elif choice == "4":
            ship_name = input("Nom du vaisseau à vérifier : ").strip()
            ship = current_fleet.find_spaceship(ship_name)
            if not ship:
                print(f"Erreur : Vaisseau introuvable.")
                continue
            ready = ship.check_preparation()
            if ready:
                print(f"Le vaisseau {ship.name} est prêt pour la mission !")
            else:
                print(
                    f"Le vaisseau {ship.name} n'est PAS prêt (il manque un pilote et/ou un technicien)."
                )

        elif choice == "5":
            try:
                name = input("Nom du nouveau vaisseau : ").strip()
                ship_type = input(
                    "Type de vaisseau (guerre / transport / marchand) : "
                ).strip()
                condition = (
                    input("État (opérationnel / endommagé) [opérationnel] : ").strip()
                    or "opérationnel"
                )

                new_ship = Spaceship(name, ship_type, condition)
                current_fleet.add_spaceship(new_ship)
                print(f"Succès : Vaisseau {new_ship.name} ajouté à la flotte.")
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choice == "6":
            current_fleet.statistics()

        elif choice == "7":
            filename = (
                input("Fichier de sauvegarde [fleet.json] : ").strip() or "fleet.json"
            )
            try:
                save_fleet(current_fleet, filename)
            except Exception as e:
                print(f"Erreur lors de la sauvegarde : {e}")

        elif choice == "8":
            filename = (
                input("Fichier à charger [fleet.json] : ").strip() or "fleet.json"
            )
            try:
                # Si le chargement réussit, on met à jour la flotte active
                current_fleet = load_fleet(filename)
                print(
                    f"Succès : Flotte « {current_fleet.name} » chargée depuis « {filename} »."
                )
            except ValueError as e:
                # Si le fichier est absent, corrompu ou incomplet, on intercepte et on conserve l'ancienne flotte
                print(f"Chargement impossible : {e}")

        else:
            print("Choix invalide. Veuillez entrer un nombre entre 0 et 9.")


if __name__ == "__main__":
    main()
