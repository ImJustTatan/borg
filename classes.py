#############		for borg
#  classes  #		by tatan
#############
from termcolor import colored, cprint
import colorama
import random
import json

colorama.init()

with open("sphrases.json") as sph: # sphrases = special phrases
    sphrases = json.load(sph)

larrow = colored('>', 'green', attrs=['bold']) # for user input
actmessages = colored('\nCurrently available actions:', 'green', attrs=['bold'])

class Weapon(object):
	"""Weapon item."""
	def __init__(self, name, desc, attk, hp):
		self.name = name
		self.desc = desc
		self.attkm = attk
		self.hp = hp
		if self.hp <= 0:
			self.attkm = 0
		self.attks = self.attkm*2

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
 		if self.hp <= -1:
 			self.hp = 0

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
 		cprint('\nThe {} has taken {} points of damage! Remaining HP: {}'.format(colored(self.name, attrs=['bold']), colored(str(hpm), 'green', attrs=['bold']), colored(str(self.hp), 'green', attrs=['bold'])))
 		if self.hp <= 0:
 			self.chstate('dead')

if __name__ == "__main__":
    cprint('This file is for borg.py, if you\'re trying to run the game then run that script.', attrs=['bold'])
    exit()