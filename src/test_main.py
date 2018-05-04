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
        pprint( list( map( lambda x : vars(x), heroes) ) )

    def test_import(self):
        mod = load_dynamic("/home/d0naim/dev/virtual-box/assets/base.py")
        print (mod)

        h = Hero(0) 
        b = mod.Base(h)
        b.on_die()

    def test_load_card(self):
        hero = Hero(0)
        load_card_for_hero(hero, "/home/d0naim/dev/virtual-box/assets/minion_card.py")
        
    

