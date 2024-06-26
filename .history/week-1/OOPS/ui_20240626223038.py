class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, other_character):
        other_character.health -= self.attack_power
        print(f"{self.name} attacks {other_character.name} for {self.attack_power} damage.")
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack Power: {self.attack_power})"
class Player(Character):
    def __init__(self, name, health, attack_power, level=1):
        super().__init__(name, health, attack_power)
        self.level = level

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack_power += 2
        print(f"{self.name} leveled up to level {self.level}!")

    def __str__(self):
        return f"{self.name} (Level: {self.level}, Health: {self.health}, Attack Power: {self.attack_power})"
class Enemy(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
def main():
    
    player = Player("Hero", 100, 15)
    print(player)

    
    enemy = Enemy("Goblin", 50, 10)
    print(enemy)

    
    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)

        print(player)
        print(enemy)

    
    if player.is_alive():
        print(f"{player.name} won the battle!")
        player.level_up()
    else:
        print(f"{enemy.name} won the battle!")

if __name__ == "__main__":
    main()
