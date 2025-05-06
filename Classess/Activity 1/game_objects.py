class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name    # Store the player's name
        self.race = race    # Store the player's race
        self.cls = cls      # Store the player's class
        self.atk = atk      # Store the player's attack power
        self.health = health # Store the player's health points

class Weapon:
    def __init__(self, name, category, damage):
        self.name = name      # Store the weapon's name
        self.category = category # Store weapon category
        self.damage = damage  # Store weapon damage

class Enemy:
    def __init__(self, name, race, damage, health):
        self.name = name      # Store enemy's name
        self.race = race      # Store enemy's race
        self.damage = damage  # Store enemy's damage
        self.health = health  # Store enemy's health