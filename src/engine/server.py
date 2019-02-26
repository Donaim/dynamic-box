
import messanger

ENCODING = 'ascii'

class Server:
	def __init__(self, ip: str, port: int):
		self.speaker = None
		self.ip = ip
		self.port = port
		self._requests = {}

	def _recieve_responce(self, client_address, data: bytes):
		s = data.decode(encoding=ENCODING)
		print('server got s:\n{}\n\n'.format(s))

	def init_speaker(self):
		if not self.speaker is None:
			raise Exception("Speaker is already initialized")

		self.speaker = messanger.Speaker(self.ip, self.port)

		self.speaker.listen(self._recieve_responce)
