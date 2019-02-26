
# from logics.board import *
# from logics.hero import *
# from logics.hand import *
# from logics.card import *

from actions import *

class PlayerSpeaker(GameSpeaker):
	def __init__(self, id: int, server_ip: str, server_port: int):
		super(PlayerSpeaker, self).__init__(server_ip=server_ip, server_port=server_port)
		self.id = id

	@server_method
	def click_board(self, player_id: int, leftclick: bool, x: int, y: int):
		''' hello here '''

		print('I klicked board!!')
		return 42

	@server_method
	def press_key(self, player_id: int, key: str):
		''' hi there '''
		pass

	@server_method
	def make_card_proposal(self, player_id: int, code: str):
		return 2

	@server_method
	def respond_to_card_proposal(self, player_id: int, proposal_id: int, answer: str):
		pass

import server

serv = server.Server('127.0.0.1', 7731)
serv.init_speaker()

sp = PlayerSpeaker(0, '127.0.0.1', 7731)
sp.init_speaker(None)
x = sp.click_board(2, True, 1, y=2)

print('x = {}'.format(x))

import time
time.sleep(100)

