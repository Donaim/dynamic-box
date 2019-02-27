
import sys

def trace(message: str):
	print(message + '\n\n')

def error(message: str):
	print('[ERROR] ' + message, file=sys.stderr)

