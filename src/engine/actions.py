
import abc
import inspect
from collections import OrderedDict

def server_method(method):
	sign = inspect.signature(method)
	params = list(OrderedDict(sign.parameters).keys())

	print('params = {}'.format(params))

	def clojured(*args, **kwargs):
		player_id = kwargs['player_id'] if 'player_id' in kwargs else args[0]

		dd = {'player_id': player_id}

		for (i, a) in enumerate(args):
			dd[params[i]] = a

		for key in kwargs:
			dd[key] = kwargs[key]

		print('passing args=<{}>; kwargs=<{}>; '.format(args, kwargs))
		print('dd = {};'.format(dd))
		return method(*args, **kwargs)

	# print('ret = {}\n'.format(method(None))
	print('doc:\n{}\n'.format(inspect.getdoc(method)))

	return clojured
	# return method

class GameSpeaker:

	def __init__(self):
		self.id = 202

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


def method_to_json(method) -> str:
	raise NotImplementedError()


sp = GameSpeaker()
x = sp.click_board(2, True, 1, y=2)

print('x = {}'.format(x))

