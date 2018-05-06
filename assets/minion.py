
from logics.unit import *

class Minion(Unit):

    def __init__(self):
        self.attack = 0

    def hit(target: Unit):
        target.on_receive_damage(self.attack)



