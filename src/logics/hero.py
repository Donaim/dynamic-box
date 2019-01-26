
from logics.board import *
from logics.hand import *

class Hero:

	def __init__(self, id: int):
		self.id = id
		self.money = 1000

		self.board = Board(self)
		self.hand = Hand(self)

