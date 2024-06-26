class AnimeCharacter:
    def attack(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Naruto(AnimeCharacter):
    def attack(self):
        return "Naruto uses Rasengan!"

class Sasuke(AnimeCharacter):
    def attack(self):
        return "Sasuke uses Chidori!"

# Function demonstrating polymorphism through duck typing
def character_attack(character):
    print(character.attack())

# Creating instances of Naruto and Sasuke
naruto = Naruto()
sasuke = Sasuke()

# Calling the character_attack function with different character objects
character_attack(naruto)  # Output: Naruto uses Rasengan!
character_attack(sasuke)  # Output: Sasuke uses Chidori!
