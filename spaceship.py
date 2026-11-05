from person import Person, Operator


class Spaceship:
    MAX_CREW = 10  # Attribut de classe

    def __init__(
        self, name: str, ship_type: str = "transport", condition: str = "opérationnel"
    ):
        self.name = name.strip()
        self.ship_type = ship_type.strip()
        self.condition = condition.strip()
        self.crew = []  # Composition : liste d'objets Person (Operator / Mentalist)

    def find_member(self, name: str):
        name_clean = name.strip().lower()
        for member in self.crew:
            if (
                member.name.lower() == name_clean
                or member.first_name.lower() == name_clean
                or (member.last_name and member.last_name.lower() == name_clean)
            ):
                return member
        return None

    def add_member(self, member: Person):
        if len(self.crew) >= self.MAX_CREW:
            raise ValueError(f"Le vaisseau {self.name} est plein.")
        if self.find_member(member.name) is not None:
            raise ValueError(f"Membre '{member.name}' déjà à bord.")
        self.crew.append(member)

    def remove_member(self, name: str):
        member = self.find_member(name)
        if member is not None:
            self.crew.remove(member)
            return member
        return None

    def check_preparation(self) -> bool:
        has_pilote = False
        has_technicien = False
        for member in self.crew:
            if isinstance(
                member, Operator
            ):  # Utilisation d'isinstance pour cibler les rôles
                if member.role == "pilote":
                    has_pilote = True
                elif member.role == "technicien":
                    has_technicien = True
        return has_pilote and has_technicien

    def watch_round(self):
        for member in self.crew:
            if hasattr(member, "act"):
                member.act()

    def to_dict(self) -> dict:
        # La composition délage la sérialisation à chaque membre
        return {
            "name": self.name,
            "ship_type": self.ship_type,
            "condition": self.condition,
            "crew": [member.to_dict() for member in self.crew],
        }

    def __str__(self) -> str:
        return f"{self.name} ({self.ship_type}, {self.condition}) – {len(self.crew)} membres"
