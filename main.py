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

larrow = colored('>', 'green', attrs=['bold']) # for user input
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
 	def __init__(self, name, desc, hp, state):
 		self.name = name
 		self.desc = desc
 		self.hp = hp
 		if state == None:
 			self.state = str(state).lower()
 		else:
 			self.state = 'alive'
 		if self.hp <= 0:
 			self.state == 'dead'
 		else:
 			self.state == 'alive'
 	def chstate(self, s):
 		"""Changes the enemy's state to the one given by the parameter 's'."""
 		self.state = s.lower()
 		if s == 'dead':
 			self.hp = 0
 			cprint('\nYou killed the {}.'.format(self.name), 'red', attrs=['bold'])
 		else:
 			self.hp = self.hp
 	def shstate(self):
 		"""Displays the enemy's state."""
 		if self.state == 'dead':
 			cprint('\nThe {} is dead. {}.'.format(self.name, sphrases["dstatements"][random.randint(0, 4)]), attrs=['bold'])
 		elif self.state == 'alive':
 			cprint('\n{}'.format(self.desc), attrs=['bold'])
 		else:
 			cprint('An error occured when trying to show this enemy\'s state.')
 	def ghit(self, hpm1, hpm2):
 		"""Function to get hit. 'hpm' is the amount of HP taken."""
 		hpm = random.randint(hpm1, hpm2)
 		self.hp -= hpm
 		cprint('\nThe {} has taken {} points of damage!'.format(colored(self.name, attrs=['bold']), colored(str(hpm), 'green', attrs=['bold'])))
 		if self.hp <= 0:
 			self.chstate('dead')


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

os.system('title Borg! v0.1b')
os.system('cls')
doggy = Enemy('Tame Dog', 'A tame and cute dog. It has a pink collar.', 10, 'alive')
print('You decide to go on an adventure, even after your mom told you you\'re too weak for this. You walk far from home, with nothing but an used kitchen knife.')
cprint('While walking, you find a {}. It has a cute pink collar.'.format(doggy.name), attrs=['bold'])

dacts('HIT, AVOID, EXAMINATE, EXIT')

while True:
	choice1 = plinput()
	error = False
	if choice1.lower().startswith('hit'):
		if choice1.lower() == 'hit tame dog':
			doggy.ghit(2, 4)
			pass
		elif choice1.lower() == 'hit':
			cprint('\nYou must specify who to hit.', 'red', attrs=['bold'])
			error = True
			pass
		else:
			cprint('\nI did not get whoever you were trying to hit.', 'red', attrs=['bold'])
			error = True
			pass
	elif choice1.lower() == 'avoid':
		chance = borg('You successfully avoided the {}!'.format(doggy.name), 'The {} blocked the path.'.format(doggy.name))
		if chance == 1:
			break
		elif chance == 2:
			pass
	elif choice1.lower().startswith('examinate'):
		if choice1.lower() == 'examinate tame dog':
			doggy.shstate()
			pass
		elif choice1.lower() == 'examinate':
			cprint('\nYou must specify what to examinate.', 'red', attrs=['bold'])
			error = True
			pass
		else:
			cprint('\nI did not get whatever you were trying to examinate.', 'red', attrs=['bold'])
			error = True
			pass
	elif choice1.lower().startswith('exit'):
		cprint('\nYou exited.', 'red', attrs=['bold'])
		exit()
	else:
		cprint('\nSorry, but I didn\'t understand you.', 'red', attrs=['bold'])
		error = True
		pass
	if doggy.state == 'dead':
		break
	if error == True:
		continue
	turn = borg('> The dog purrs.', '> The dog mooes violently!')