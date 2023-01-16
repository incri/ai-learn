'''
In this program, we are trying to pass argument/parameter from terminal to
the program. The argument can be 'add' or 'divide'. Depending the argument 
value, either the add or divide function will be called.
'''

import sys
		
def add(first, second):
	return first + second

def divide(numerator, denominator):
	return numerator / denominator

def main():
	args = sys.argv[1:]

	first = int( input('Please enter first number:\n'))
	second = int( input('Please enter second number:\n'))

	if (args[0] == 'add'):		
		print('Addition of', first, 'and', second, 'results into', add(first, second), '.')

	elif (args[0] == 'divide'):
		print('Division of', first, 'by', second, 'results into', divide(first, second), '.')
	
if __name__ == "__main__":
    main()


