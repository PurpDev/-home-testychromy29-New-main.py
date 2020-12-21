class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo,  "/ Points de vie:", health, "/ Attack:", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -=  damage

    def attack_player(self, target_player):
        damage = self.attack

        if self.has_weapon():
           #add weapon damages to attack value
              damage += self.weapon.get_damage_amount()

        target_player.damage(damage)


    # switch weapon status
    def set_weapon(self, weapon):
        self.weapon = weapon

    #check if player got a weapon
    def has_weapon(self):
        return self.weapon is not None
