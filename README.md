# Projet Fondation - 4PYTH (Fil Rouge)

**Auteur :** Akadus DAGBEKPO M1-CYBER  
**École :** École Supérieure d'Informatique (École Hexagone)  
**Module :** 4PYTH - Langage Python  

---

## 🚀 Description du projet
Ce projet consiste à développer une application de gestion de flotte spatiale et de ses équipages (inspirée de l'univers de *Fondation*). Il a été construit progressivement à travers trois TP pour mettre en pratique la programmation orientée objet (POO), l'héritage, la composition, l'encapsulation, ainsi que la persistance des données au format JSON avec une gestion rigoureuse des erreurs.

---

## 📁 Structure du projet (8 fichiers Python)
Le code est réparti de manière modulaire selon le principe de responsabilité unique :
- `person.py` : Contient la classe mère `Person` et ses classes filles `Operator` et `Mentalist` (gestion de l'héritage, des propriétés `@property` et de la conversion en dictionnaire).
- `spaceship.py` : Gère la classe `Spaceship` (composition avec l'équipage, vérification de la préparation du vaisseau).
- `fleet.py` : Gère la classe globale `Fleet` et le calcul des statistiques.
- `crew.py` : Contient la fonction `build_fleet` pour reconstruire les objets à partir de dictionnaires ou de fichiers JSON.
- `fleet_data.py` : Contient le jeu de données initial de la flotte `Galactica`.
- `storage.py` : Gère la sauvegarde (`save_fleet`) et le chargement sécurisé (`load_fleet`) en JSON.
- `main.py` : Point d'entrée principal du programme avec le menu interactif.
- `test_classes.py` : Script de test unitaire pour valider le comportement des classes.

---

## ⚙️ Comment lancer le programme

1. Activer l'environnement virtuel dans votre terminal :
   ```bash
   # Sur Windows (invite de commandes ou PowerShell)
   .venv\Scripts\activate

   # Sur Mac / Linux
   source .venv/bin/activate# Projet Fondation