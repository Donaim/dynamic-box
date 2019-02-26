
# from logics.board import *
# from logics.hero import *
# from logics.hand import *
# from logics.card import *

from actions import *

class PlayerSpeaker(GameSpeaker):
	def __init__(self, id: int, server_ip: str, server_port: int):
		super(PlayerSpeaker, self).__init__(server_ip=server_ip, server_port=server_port)
		self.player_id = id

	@server_method
	def click_board(self, leftclick: bool, x: int, y: int):
		''' hello here '''

		print('I klicked board!!')
		return 42

	@server_method
	def press_key(self, key: str):
		''' hi there '''
		pass

	@server_method
	def make_card_proposal(self, code: str):
		return 2

	@server_method
	def respond_to_card_proposal(self, proposal_id: int, answer: str):
		pass


def kek():
	import server

	serv = server.Server('127.0.0.1', 7731)
	serv.init_speaker()

	sp = PlayerSpeaker(0, '127.0.0.1', 7731)

	# print(sp._get_child_state())


	sp.init_speaker(None)
	x = sp.click_board(True, 1, y=2)

	print('x = {}'.format(x))

	import time
	time.sleep(2)

	sp.stop()
	serv.stop()

if __name__ == '__main__':
	kek()
