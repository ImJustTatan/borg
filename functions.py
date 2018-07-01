###############		functions for borg
#  functions  #		by tatan
###############
from termcolor import colored, cprint
import colorama
import random

colorama.init()

larrow = colored('>', 'green', attrs=['bold']) # for user input
actmessages = colored('\nCurrently available actions:', 'green', attrs=['bold'])

def plinput():
	"""Requests player input (for commands)."""
	print('\n{}'.format(larrow), end='\0')
	r = input()
	return r

def dacts(m):
	"""Displays available commands (given by the only parameter)."""
	if m == None:
		cprint('\nNo actions are available!', 'red', attrs=['bold'])
	else:
		print(actmessages, end='\0')
		print('{}.'.format(m))

def borg(mtrue, mfalse):
	"""Function for various situations. The parameters are the returned messages for each case."""
	chance = random.randint(1, 2)
	if chance == 1:
		cprint('\n{}'.format(mtrue), 'green', attrs=['bold'])
		return 1
	elif chance == 2:
		cprint('\n{}'.format(mfalse), 'red', attrs=['bold'])
		return 2

if __name__ == "__main__":
    cprint('This file is for borg.py, if you\'re trying to run the game then run that script.', attrs=['bold'])
    exit()