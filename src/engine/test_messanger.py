
import unittest
import time

from messanger import *

class TestC1(unittest.TestCase):

	def test_random(self):
		import random
		print(random.randint(1, 10))

	def test_send_recieve(self):
		def callback(data: str):
			print ("Test got '{}'".format(data))

		s = connect_listen(callback)
		send_message(b"Hello :)")

		time.sleep(1)

		s.close()

