import os
import sys

class Exit:
	sweet = 0
	error = 1

def main():
	print("Hello user %s ... \n" %sys.argv[1])
	sys.exit(Exit.sweet)

main()
