
import asyncore
import socket
import logging

import threading
from threading import Thread

# TCP_IP = '127.0.0.1'
TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def _listen_conn(connection, client_address, func):
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

		func(data)

	connection.close()
	print ("Closed connection {}".format(client_address))

def _accept_loop(sock, func):
	print ("Started listening")
	while True:
		try:
			conn, addr = sock.accept()
			th = Thread(target=_listen_conn, args=(conn, addr, func, ))
			th.start()
		except socket.timeout:
			continue
		except Exception as ex:
			break

# Returns cancellation token
def connect_listen(func):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# This is important or will block otherwise
	sock.settimeout(0.1)

	# Bind the socket to the port
	server_address = (TCP_IP, TCP_PORT)
	print('starting up on {} port {}'.format(*server_address))
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)

	# Delegate listening to separate thread
	thst = Thread(target=_accept_loop, args=(sock, func, ))
	thst.start()

	return sock

def send_message(mess: str):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(mess)
	s.close()
	print ("Sending done")
