ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]

ACTIONS = {
    "commandant": "donne ses ordres à l'équipage",
    "pilote": "pilote le vaisseau",
    "technicien": "répare les moteurs",
    "armurier": "vérifie les canons",
    "marchand": "négocie une cargaison",
    "entretien": "nettoie le vaisseau",
}


class Person:
    def __init__(
        self, first_name: str, last_name: str = "", gender: str = "M", age: int = 0
    ):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.gender = gender
        self.age = age

    @property
    def name(self) -> str:
        # Propriété calculée : assemble le nom complet proprement
        return f"{self.first_name} {self.last_name}".strip()

    def introduce_yourself(self) -> str:
        genre_str = "un homme" if self.gender.upper() in ["M", "H"] else "une femme"
        return f"Je m'appelle {self.name}, je suis {genre_str} de {self.age} ans."

    def to_dict(self) -> dict:
        # Sérialisation de base pour le JSON
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "age": self.age,
        }

    def __str__(self) -> str:
        return f"{self.name} ({self.gender}, {self.age} ans)"


class Operator(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str = "",
        gender: str = "M",
        age: int = 0,
        role: str = "pilote",
        experience: int = 0,
    ):
        super().__init__(first_name, last_name, gender, age)
        self.role = role  # Passe par le setter pour valider le rôle
        self.experience = experience

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, new_role: str):
        role_clean = new_role.lower().strip()
        if role_clean not in ROLES:
            raise ValueError(f"rôle inconnu : {new_role}")  # Sécurité : liste blanche
        self._role = role_clean

    @property
    def experience(self) -> int:
        return self._experience

    @experience.setter
    def experience(self, value: int):
        self._experience = max(0, min(value, 100))  # Borne l'expérience

    def gain_experience(self):
        self.experience += 1

    def act(self):
        action = ACTIONS.get(self.role, "effectue une tâche")
        print(f"{self.name} {action}.")
        self.gain_experience()

    def to_dict(self) -> dict:
        d = super().to_dict()  # Réutilise la classe mère (Évite la redondance)
        d["type"] = "Operator"
        d["role"] = self.role
        d["experience"] = self.experience
        return d

    def __str__(self) -> str:
        return f"{super().__str__()} – {self.role}"


class Mentalist(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str = "",
        gender: str = "F",
        age: int = 0,
        mana: int = 100,
    ):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = max(0, min(value, 100))  # Le mana reste toujours entre 0 et 100

    def influence(self, target: Person):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} influence {target.name}.")
            if hasattr(target, "act"):
                target.act()
        else:
            print(f"{self.name} n'a pas assez de mana…")

    def recharge_mana(self):
        self.mana += 50

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["type"] = "Mentalist"
        d["mana"] = self.mana
        return d

    def __str__(self) -> str:
        return f"{super().__str__()} – mentaliste, {self.mana} mana"
