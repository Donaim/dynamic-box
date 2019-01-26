
import socket, sys
from threading import Thread

# TCP_IP = '127.0.0.1'
TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def _listen_conn(connection, client_address, func):
	# Receive the data in small chunks and retransmit it
	while True:
		data = connection.recv(16)
		print('received {!r}'.format(data))
		if data:
			func(data)
		else:
			print('no data from', client_address)
			break

	print ("Connection is closing".format(client_address))
	connection.close()
	print ("Connection [{}] closed".format(client_address))

def _accept_loop(sock, func):
	while True:
		try:
			conn, addr = sock.accept()
			print('connection from', addr)
			th = Thread(target=_listen_conn, args=(conn, addr, func, ))
			th.start()
		except ex:
			print ("Exception {} ".format(ex))

def _listen_loop_starter(sock, func):
	th = Thread(target=_accept_loop, args=(sock, func, ))
	th.start()

	# th.start()
	# th.join()
	import time
	time.sleep(2)
	# sock.close()
	sock.shutdown(socket.SHUT_WR)
	print ("closed a socket")

# Returns cancellation token
def connect_listen(func):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = (TCP_IP, TCP_PORT)
	print('starting up on {} port {}'.format(*server_address))
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)

	print ("Started listening")

	thst = Thread(target=_listen_loop_starter, args=(sock, func, ))
	thst.start()

def send_message(mess: str):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(mess)
	s.close()
	print ("Sending done")
