
from logics.hero import *
from logics.unit import *

class Base(Unit):

    def __init__(self, owner : Hero):
        self.owner = owner

    def on_die(self):
        print ("Player {} lost.".format(self.owner.id))

