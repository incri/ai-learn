"""
In this program, we are building a structure with main function

To run this program, type following in terminal

python 01-hello_world.py hi lucky

Then see the result.
"""

import sys

'''
The first line with multi-line comment after the function name
serves as documentation of the function.
'''
def hello_world():
	'''	A sample hello world function	'''
	print("Hello world!")			


def main():
	args = sys.argv[1:]		# sys.argv provides list of arguments passed
						# By using [1:], we are accessing data from
						# index 1 till end of the list
	hello_world()

	for arg in args:			# using for loop to iterate over items in the list
	 		print(arg)

	print(hello_world.__doc__)	# accessing the documentation of hello_world function
						# defined above

if __name__ == "__main__":
    main()