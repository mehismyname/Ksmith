import sys
import time

__all__= ['hello', 'delay_print']

def hello(name):
	print(f"Hello (name), my name is Kent Smith")

def delay_print(s, end='\n'):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.04)
	print('end')

def get_int(prompt="Enter a number", start='0', finish='0'):
	#
	while True:
		try:
			x=int(input(f"{prompt}:"))
		except ValueError:
			print("Please enter an integer!")
		if finish != 0:
			if start != 0:
				if x < finish and x > start:
					break
			if x < finish:
				break
		else:
			print(f"Enter a Value between {start} and {finish}")
