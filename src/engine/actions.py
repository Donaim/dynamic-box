
import inspect
import json

def server_method(method):
	sign = inspect.signature(method)
	params = list(sign.parameters.keys())
	params = params[1:] # Skip `self'

	print('params = {}'.format(params))

	def clojured(self, *args, **kwargs):
		dd = {}

		for (i, a) in enumerate(args):
			dd[params[i]] = a

		for key in kwargs:
			dd[key] = kwargs[key]

		js = json.dumps(dd, check_circular=False)

		print('passing args=<{}>; kwargs=<{}>; '.format(args, kwargs))
		print('id = {}'.format(self.id))
		print('dd = {};'.format(js))
		return method(self, *args, **kwargs)

	return clojured

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

