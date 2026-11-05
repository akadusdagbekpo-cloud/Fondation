from person import Operator, Mentalist
from spaceship import Spaceship

# 1. Création des membres
bel = Operator("Bel", "Riose", "M", 48, "commandant")
hugo = Operator("Hugo", "Crast", "M", 37, "pilote")
joie = Mentalist("Joie", "", "F", 25)

# 2. Présentations
print(bel.introduce_yourself())  
print(joie.introduce_yourself()) 
print(hugo)  
print(joie) 

# 3. Action et expérience
hugo.act() 
print(hugo.experience)  

# 4. Influence du mentaliste (6 fois)
for _ in range(6):
    joie.influence(hugo)

print(joie.mana)  

# 5. Recharge de mana
joie.recharge_mana()
joie.recharge_mana()
joie.recharge_mana()
print(joie.mana) 

# 6. Gestion du vaisseau et vérification de la préparation
ship = Spaceship("Fearless", "guerre")
ship.add_member(bel)
ship.add_member(hugo)
print(ship.check_preparation()) 

ship.add_member(Operator("Yugo", "Amary", "M", 33, "technicien"))
print(ship.check_preparation())  
print(ship)  

# 7. Test de levée d'exception pour un rôle invalide
try:
    Operator("Eve", "Hacker", "F", 30, "root")
except ValueError as e:
    print(f"ValueError: {e}")
