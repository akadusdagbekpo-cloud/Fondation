import json
from crew import build_fleet


def save_fleet(fleet, path="fleet.json"):
    # Écriture propre : encodage UTF-8 et indentation lisible
    data = fleet.to_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Flotte sauvegardée dans « {path} ».")


def load_fleet(path="fleet.json"):
    # Chargement robuste : intercepte chaque type d'erreur sans crasher
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise ValueError(f"aucune sauvegarde « {path} »")
    except json.JSONDecodeError:
        raise ValueError(f"la sauvegarde « {path} » est corrompue")

    try:
        return build_fleet(data)
    except KeyError:
        raise ValueError(f"la sauvegarde « {path} » est incomplète")
    except ValueError as e:
        raise e  # Remonte l'erreur métier de la classe (ex: rôle inconnu)
