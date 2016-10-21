#!/usr/bin/env python3

from colorama import Fore, Back 
import readline
import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}

def calculate(myarg1):
	print(Back.BLACK+Fore.BLUE+myarg1)
	stack = list()
	for token in myarg1.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = operators[token]
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError
	return stack.pop()

def main():
	while True:
		calculate(input(Back.WHITE+Fore.GREEN+"rpn calc> "+Back.BLACK+Fore.GREEN))

if __name__ == '__main__':
	main()

