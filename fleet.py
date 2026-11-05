from spaceship import Spaceship
from person import Operator, Mentalist


class Fleet:
    MAX_SPACESHIPS = 15

    def __init__(self, name: str):
        self.name = name.strip()
        self.spaceships = []  # Composition : liste d'objets Spaceship

    def find_spaceship(self, name: str) -> Spaceship:
        name_clean = name.strip().lower()
        for ship in self.spaceships:
            if ship.name.lower() == name_clean:
                return ship
        return None

    def add_spaceship(self, spaceship: Spaceship):
        if len(self.spaceships) >= self.MAX_SPACESHIPS:
            raise ValueError(f"Flotte {self.name} pleine.")
        if self.find_spaceship(spaceship.name) is not None:
            raise ValueError(f"Vaisseau '{spaceship.name}' déjà présent.")
        self.spaceships.append(spaceship)

    def statistics(self):
        total_ships = len(self.spaceships)
        total_members = 0
        role_counts = {}
        mentalist_count = 0
        total_operator_exp = 0
        operator_count = 0
        ready_ships = 0

        for ship in self.spaceships:
            total_members += len(ship.crew)
            if ship.check_preparation():
                ready_ships += 1

            for member in ship.crew:
                if isinstance(member, Mentalist):
                    mentalist_count += 1
                elif isinstance(member, Operator):
                    operator_count += 1
                    total_operator_exp += member.experience
                    role_counts[member.role] = role_counts.get(member.role, 0) + 1

        avg_exp = (total_operator_exp / operator_count) if operator_count > 0 else 0.0

        print(f"=== Statistiques de la flotte '{self.name}' ===")
        print(f"Vaisseaux : {total_ships}/{self.MAX_SPACESHIPS} ({ready_ships} prêts)")
        print(f"Membres : {total_members} (dont {mentalist_count} mentalistes)")
        print(f"Expérience moyenne des opérateurs : {avg_exp:.1f}")
        print("Rôles des opérateurs :")
        if role_counts:
            for role, count in role_counts.items():
                print(f"  - {role} : {count}")
        else:
            print("  - Aucun opérateur")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "spaceships": [ship.to_dict() for ship in self.spaceships],
        }
