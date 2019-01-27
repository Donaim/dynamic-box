
from logics.board import *
from logics.hero import *
from logics.hand import *
from logics.card import *

import messanger
import random
import binencoder
import json

ENCODING='ascii'

class PlayerSpeaker:
	def __init__(self, id: int, server_ip: str, server_port: int):
		self.id = id
		self.speaker = None
		self.server_ip = server_ip
		self.server_port = server_port
		self._requests = {}

	def _send_json(self, obj: dict, callback):
		request_id = random.randint(0, 9999)
		obj['request_id'] = request_id
		self._requests[request_id] = (obj, callback)

		encoded = json.dumps(obj, check_circular=False)
		bi = bytes(encoded, encoding=ENCODING)
		self.speaker.send(bi, self.server_ip, self.server_port)

	def _recieve_responce(self, client_address, data: bytes):
		s = data.decode(encoding=ENCODING)
		decoded = json.loads(s, encoding=ENCODING)

		request_id = decoded['request_id']
		(obj, callback) = self._requests[request_id]

		# There is no synchronization from our side required
		# since we are using TCP that does that part
		callback(request=obj, responce=decoded)

	def init_speaker(self, callback):
		if not self.speaker is None:
			raise Exception("Speaker is already initialized")

		self.speaker = messanger.Speaker('localhost', 5009)

		self.speaker.listen(self._recieve_responce)

		self._send_json({'from': self.id, 'type': 'init'}, callback=callback)

	def click_board(self, callback, leftclick: bool, x: int, y: int):
		self._send_json({'from': self.id, 'type': 'click_board', 'leftclick': leftclick, 'x': x, 'y': y},
		                callback=callback)

	def press_key(self, callback, key: str):
		self._send_json({'from': self.id, 'type': 'press_key', 'key': key},
		                callback=callback)

	def make_card_proposal(self, code: str):
		self._send_json({'from': self.id, 'type': 'make_card_proposal', 'code': code},
		                callback=callback)

	def respond_to_card_proposal(self, callback, proposal_id: int, answer: str):
		self._send_json({'from': self.id, 'type': 'respond_to_card_proposal', 'proposal_id': proposal_id, 'answer': answer},
		                callback=callback)
