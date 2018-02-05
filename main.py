"""A terminal RPG for Windows. By Tatan."""

#####################
#  imports n stuff  #
#####################

from termcolor import colored, cprint
import colorama
import winsound # for later versions
import random
import json
import os

colorama.init()

##############
#  keywords  #
##############

larrow = colored('>', 'green') # for user input
actmessages = colored('\nCurrently available actions:', 'green', attrs=['bold'])

##################
#  json configs  #
##################

with open("sphrases.json") as sph: # sphrases = special phrases
    sphrases = json.load(sph)

#############
#  classes  #
#############

class Enemy(object):
 	"""Enemies (and sometimes not-so-enemies) you find in the adventure."""
 	def __init__(self, name, desc, state):
 		self.name = name
 		self.desc = desc
 		if state == None:
 			self.state = str(state).lower()
 		else:
 			self.state = 'alive'
 	def chstate(self, s):
 		"""Changes the enemy's state to the one given by the parameter 's'."""
 		self.state = s.lower()
 		if s == 'dead':
 			cprint('\nYou killed the {}.'.format(self.name), 'red', attrs=['bold'])
 	def shstate(self):
 		"""Displays the enemy's state."""
 		if self.state == 'dead':
 			print('\nThe {} is dead. {}.'.format(self.name, sphrases["dstatements"][random.randint(0, 4)]))
 		elif self.state == 'alive':
 			print('\n{}'.format(self.desc))
 		else:
 			cprint('An error occured when trying to show this enemy\'s state.')


###############
#  functions  #
###############

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

##############
#  the game  #
##############

os.system('cls')
doggy = Enemy('Tame Dog', 'A tame and cute dog. It has a pink collar.', 'alive')
print('You decide to go on an adventure, even after your mom told you you\'re too weak for this. You walk far from home, with nothing but an used kitchen knife.')
cprint('While walking, you find a {}. It has a cute pink collar.'.format(doggy.name), attrs=['bold'])

dacts('KILL, AVOID, EXIT')

while True:
	choice1 = plinput()
	if choice1.lower().startswith('kill'):
		if choice1.lower() == 'kill tame dog':
			doggy.chstate('dead')
			break
		elif choice1.lower() == 'kill':
			cprint('\nYou must specify who to kill.', 'red', attrs=['bold'])
			pass
		else:
			cprint('\nI did not get whoever you were trying to kill.', 'red', attrs=['bold'])
			pass
	elif choice1.lower() == 'avoid':
		chance = borg('You successfully avoided the {}!'.format(doggy.name), 'The {} blocked the path.'.format(doggy.name))
		if chance == 1:
			break
		elif chance == 2:
			pass

	elif choice1.lower().startswith('exit'):
		cprint('\nYou exited.', 'red', attrs=['bold'])
		exit()
	else:
		cprint('\nSorry, but I didn\'t understand you.', 'red', attrs=['bold'])
		pass
	turn = borg('> The dog purrs.', '> The dog mooes violently!')
