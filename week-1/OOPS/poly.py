class AnimeCharacter:
    def attack(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Naruto(AnimeCharacter):
    def attack(self):
        return "Naruto uses Rasengan!"

class Sasuke(AnimeCharacter):
    def attack(self):
        return "Sasuke uses Chidori!"


def character_attack(character):
    print(character.attack())


naruto = Naruto()
sasuke = Sasuke()

character_attack(naruto)  
character_attack(sasuke)  
