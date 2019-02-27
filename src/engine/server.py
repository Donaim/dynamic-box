
import messanger

import enlog

ENCODING = 'ascii'

class Server:
	def __init__(self, ip: str, port: int):
		self.speaker = None
		self.ip = ip
		self.port = port
		self._requests = {}
		self.clients = {}

	def _recieve_responce(self, client_address, package: bytes):
		s = package.decode(encoding=ENCODING)

		enlog.trace('server {} got from {} client s:\n{}'.format(self.ip, 'old' if client_address in self.clients else 'new', s))

	def init_speaker(self):
		if not self.speaker is None:
			raise Exception("Speaker is already initialized")

		self.speaker = messanger.Speaker(self.ip, self.port)

		self.speaker.listen(self._recieve_responce)

	def stop(self):
		return self.speaker.stop()
