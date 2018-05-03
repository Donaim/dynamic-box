


class Unit:
    def __init__(self, owner):
        self.owner = owner
        self.hp = 100
    
    def on_turn_end(self):
        pass

    def on_receive_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.on_die()

    def on_die(self):
        pass
