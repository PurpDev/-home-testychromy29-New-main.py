from player import Player
from weapon import Weapon

knife = Weapon("Couteau", 7)
player1 = Player("Shô", 20, 3)


player1.set_weapon(knife)
player2 = Player("Buraka", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque de plein fouet", player2.get_pseudo())

print("Bienvenue au joueur", player1.get_pseudo(),  "/ Points de vie:", player1.get_health(), "/ Attack:", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(),  "/ Points de vie:", player2.get_health(), "/ Attack:", player2.get_attack_value())
