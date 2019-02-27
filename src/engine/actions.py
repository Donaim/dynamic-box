
import inspect
import json
import random

import messanger

ENCODING='ascii'

class GameSpeaker:
	def __init__(self, server_ip: str, server_port: int):
		self._speaker = None
		self._server_ip = server_ip
		self._server_port = server_port
		self._requests = {}

	def _get_child_state(self) -> dict:
		re = {}
		for m in filter(lambda m: not m.startswith('_'), vars(self)):
			re[m] = self.__getattribute__(m)
		return re

	def _send_json(self, obj: dict, callback):
		if not self._speaker:
			raise Exception('Speaker is not initialized')

		state = self._get_child_state()
		obj = { **state, **obj }

		request_id = random.randint(0, 9999)
		obj['request_id'] = request_id
		self._requests[request_id] = (obj, callback)

		encoded = json.dumps(obj, check_circular=False)
		bi = bytes(encoded, encoding=ENCODING)
		self._speaker.send(bi, self._server_ip, self._server_port)

	def _recieve_responce(self, client_address, package: bytes):
		s = package.decode(encoding=ENCODING)
		decoded = json.loads(s, encoding=ENCODING)

		request_id = decoded['request_id']
		(obj, callback) = self._requests[request_id]

		if callback:
			# There is no synchronization from our side required
			# since we are using TCP that does that part
			callback(request=obj, responce=decoded)

	def init_speaker(self, callback):
		if not self._speaker is None:
			raise Exception("Speaker is already initialized")

		self._speaker = messanger.Speaker('localhost', 2007)

		self._speaker.listen(self._recieve_responce)

		self._send_json({'type': 'init'}, callback=callback)

	def stop(self):
		if self._speaker is None:
			raise Exception("Speaker is not initialized")

		self._send_json({'type': 'stop'}, callback=None)

		return self._speaker.stop()

def server_method(method):
	''' Encodes function call as json and sends it to server,
	then executes call '''

	sign = inspect.signature(method)
	params = list(sign.parameters.keys())
	params = params[1:] # Skip `self'

	def clojured(self: GameSpeaker, *args, **kwargs):
		dd = {}

		dd['type'] = method.__name__

		for (i, a) in enumerate(args):
			dd[params[i]] = a

		for key in kwargs:
			dd[key] = kwargs[key]

		self._send_json(obj=dd, callback=None)

		return method(self, *args, **kwargs)

	return clojured
