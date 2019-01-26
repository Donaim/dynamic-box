
import asyncore
import socket
import logging

import threading
from threading import Thread

BUFFER_SIZE = 1024

class Speaker:
	def __init__(self, ip: int, port: int):
		self.ip = ip
		self.port = port
		self.timeout = 0.1
		self.name = "Unnamed"
		self.sock = None
		self.__listening = False
		self.callback = None
		self.targets = {}

	def _listen_conn(self, connection, client_address):
		data = None
		print('connection from', client_address)
		while True:
			try:
				data = connection.recv(16)
				if not data:
					break
			except socket.timeout:
				continue
			except Exception as ex:
				break

			self.callback(data)

		connection.close()
		print ("Closed connection {}".format(client_address))

	def _accept_loop(self):
		self.__listening = True
		print ("{} started listening".format(self.name))
		while True:
			try:
				conn, addr = self.sock.accept()
				th = Thread(target=self._listen_conn, args=(conn, addr, ))
				th.start()
			except socket.timeout:
				continue
			except Exception as ex:
				break

	def listen(self, callback):
		if self.__listening:
			raise Exception("Started already")

		self.callback = callback
		
		if not self.sock:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(self.timeout)

			server_address = (self.ip, self.port)
			print('starting up on {} port {}'.format(*server_address))
			sock.bind(server_address)

			sock.listen(1)

			self.sock = sock

		self.listh = Thread(target=self._accept_loop)
		self.listh.start()

	def send(self, mess: bytes, ip: int, port: int):
		key = (ip, port)

		try:
			s = self.targets[key]
		except KeyError:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, port))
			self.targets[key] = s

		return s.send(mess)

	def closetarget(self, ip: int, port: int):
		key = (ip, port)
		s = self.targets[key]
		if not s:
			raise Exception("No such target ({}, {})".format(ip, port))

		s.close()
		self.targets[key] = None

	def stop(self):
		if self.__listening:
			self.sock.close()
			self.__listening = False
		else:
			raise Exception("Not started")

	def __del__(self):
		for target in self.targets.values():
			target.close()

		if self.__listening:
			self.stop()
