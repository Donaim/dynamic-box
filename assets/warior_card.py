
from warior import *
from minion_card import *


class WariorCard(MinionCard):

    def __init__(self):
        MinionCard.__init__(self)

        print ("WARIOR CARD CREATED!")

    def _create_target_minion(self):
        return Warior()

