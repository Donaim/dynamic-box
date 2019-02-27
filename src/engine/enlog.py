
import sys

def trace(message: str):
	print(message)

def error(message: str):
	print('[ERROR] ' + message, file=sys.stderr)

