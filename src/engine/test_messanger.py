
import unittest
import time

from messanger import *

class TestC1(unittest.TestCase):

	def test_random(self):
		import random
		print(random.randint(1, 10))

	def test_send_recieve(self):
		def callback(client_address: str, data: str):
			print ("Test got '{}'".format(data))

		s = Speaker(ip='localhost', port=1338)
		s.listen(callback)
		s2 = Speaker(ip='localhost', port=1338)

		s2.send(b"Hello :)", 'localhost', 1338)

		time.sleep(1)

		s.stop()
