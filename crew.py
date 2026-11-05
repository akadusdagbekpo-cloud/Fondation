from person import Operator, Mentalist
from spaceship import Spaceship
from fleet import Fleet


def build_fleet(data: dict) -> Fleet:
    # Factory / Rechargement de la structure objet à partir du JSON
    fleet = Fleet(data.get("name", "Flotte Inconnue"))

    for ship_data in data.get("spaceships", []):
        ship = Spaceship(
            name=ship_data["name"],
            ship_type=ship_data.get("ship_type", "transport"),
            condition=ship_data.get("condition", "opérationnel"),
        )

        for member_data in ship_data.get("crew", []):
            m_type = member_data.get("type")

            if m_type == "Operator":
                member = Operator(
                    first_name=member_data["first_name"],
                    last_name=member_data.get("last_name", ""),
                    gender=member_data.get("gender", "M"),
                    age=member_data.get("age", 0),
                    role=member_data.get("role", "pilote"),
                    experience=member_data.get(
                        "experience", 0
                    ),  # Gère la rétrocompatibilité TP2/TP3
                )
            elif m_type == "Mentalist":
                member = Mentalist(
                    first_name=member_data["first_name"],
                    last_name=member_data.get("last_name", ""),
                    gender=member_data.get("gender", "F"),
                    age=member_data.get("age", 0),
                    mana=member_data.get("mana", 100),
                )
            else:
                continue

            ship.add_member(member)

        fleet.add_spaceship(ship)

    return fleet
