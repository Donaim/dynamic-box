
from logics.card import *
from ui.questions import *


class MinionCard(Card):


	def __init__(self):
		Card.__init__(self)
		
		print ("MINION CARD CREATED!")

	def _create_target_minion(self):
		return 1
		# raise Exception("ABSTRACT METHOD HAS NOT BEEN IMPLEMENTED")

	def play(self, owner) -> bool:
		try: 
			minion = self._create_target_minion()
			(x, y) = choose_free_board_position(owner.board)
			owner.board.set(x, y, minion)
		except:
			return False

