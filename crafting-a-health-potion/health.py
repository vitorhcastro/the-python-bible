import random

health = 50

difficulty = random.randint(1, 3)
print(difficulty)

potion_health = int(random.randint(25, 50) / difficulty)
health += potion_health

print(health)
