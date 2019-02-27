
import sys

def padding(pre: str, message: str) -> str:
	lines = message.split('\n')
	first = pre + lines[0]

	pad = len(pre)
	def add_padding(line: str) -> str:
		return '\n' + (' ' * pad) + line

	return first + ''.join(map(add_padding, lines[1:]))

def trace(message: str):
	print(padding('[T] ', message))

def error(message: str):
	print(padding('[ERROR] ', message), file=sys.stderr)

