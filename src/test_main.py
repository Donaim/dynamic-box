import unittest

from logics.base import *
from logics.board import *
from logics.hero import *

class TestC1(unittest.TestCase):

    def test_random(self):
        import random
        print(random.randint(1, 10))

    def test_create(self):
        h = Hero(0) 
        b = Base(h)
        print ("Base created!")
