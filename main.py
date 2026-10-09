from crew import crew, add_member, remove_member, display_crew, check_crew


def lancer_menu():
    while True:
        print("\n===== MENU EQUIPAGE =====")
        print("1. Ajouter un membre")
        print("2. Afficher l'equipage")
        print("3. Retirer un membre")
        print("4. Verifier l'equipage")
        print("0. Quitter")

        choix = input("Votre choix : ")

        match choix:
            case "1":
                add_member(crew)
            case "2":
                display_crew(crew)
            case "3":
                remove_member(crew)
            case "4":
                check_crew(crew)
            case "0":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide.")


if __name__ == "__main__":
    lancer_menu()