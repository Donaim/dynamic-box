import unittest
import pprint

pp = pprint.PrettyPrinter()
def pprint(obj): pp.pprint(obj)

from logics.board import *
from logics.hero import *
from engine.engine import *

class TestC1(unittest.TestCase):

    def test_random(self):
        import random
        print(random.randint(1, 10))

    def test_create(self):
        h = Hero(0) 
        print ("Hero created!")

    def test_init_game(self):
        heroes = init_game(3)
        
        print("heroes:")
        pprint( list( map( vars, heroes) ) )

    def test_import(self):
        mod = load_dynamic("/home/d0naim/dev/dynamic-box/assets/base.py")
        print (mod)

        h = Hero(0) 
        b = mod.Base(h)
        b.on_die()

    def test_load_card(self):
        hero = Hero(0)
        load_card_for_hero(hero, "/home/d0naim/dev/dynamic-box/assets/minion_card.py")
        load_dynamic_to_sys("/home/d0naim/dev/dynamic-box/assets/minion.py")
        load_card_for_hero(hero, "/home/d0naim/dev/dynamic-box/assets/warior.py")

    def test_play_card(self):
        hero = Hero(0)
        card = load_card_for_hero(hero, "/home/d0naim/dev/dynamic-box/assets/minion_card.py")
        card.play(hero)

    
