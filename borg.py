"""Main executable script for Borg: A terminal RPG for Windows. By Tatan."""

#####################
#  imports n stuff  #
#####################

from pyfiglet import figlet_format
from termcolor import colored, cprint
import classes # classes.py
import functions # functions.py
import colorama
import winsound # for later versions
import random
import json # used in classes.py
import os

colorama.init()


##############
#  variables #
##############

os.environ['LINES'] = "50"
os.environ['COLUMNS'] = "80"

wpn = classes.Weapon('null', 'If you\'re reading this, congratulations! You got an error weapon which you shouldn\'t have at all!', 999, 999)

statsl1 = colored('\nNAME:         ', attrs=['bold'])
statsl2 = colored('HP:           ', attrs=['bold']) + colored('NOT IMPLEMENTED YET!', 'red')
statsl3 = colored('WEAPON:       ', attrs=['bold']) + wpn.name + '. ' + colored('WPN HP: ', attrs=['bold']) + colored(str(wpn.hp), 'green')
statsl4 = colored('WEAPON DESC.: ', attrs=['bold']) + wpn.desc

############
# the menu #
############

os.system('title borg! v0.1b')
os.system('cls')
cprint(figlet_format('b o r g !', font='alligator'), 'green', attrs=['bold'])
print(colored('\nInput your name: ', attrs=['bold']), end='\0')
pname = input()
print(colored('\nInput your age: ', attrs=['bold']), end='\0')
page = input()
print(colored('\nInput your sex (F or M): ', attrs=['bold']), end='\0')
psex = input()
cprint('\nStarting...', 'green', attrs=['bold'])
os.system('cls')

##############
#  the game  #
##############

doggy = classes.Enemy('Tame Dog', 'A tame and cute dog. It has a pink collar.', 10, 'alive')
if pname.lower().startswith('god'):
	pass
elif pname.lower() == 'link':
	wpn = classes.Weapon('Master Sword', 'A legendary magic sword with unmeasured power.', 10, 24)
else:
	wchance = random.randint(1,2) # weapon chance number
	if wchance == 1:
		wpn = classes.Weapon('Kitchen Knife', 'An used kitchen knife.', 2, 8)
	elif wchance == 2:
		wpn = classes.Weapon('Plastic Katana', 'A toy katana. Made with <3 by your dad.', 5, 10)
print('I, {0}, decided to go on an adventure, even after my mom told me I\'m too weak for this. I walk far from home, with nothing but an used {1}. My adventure begins.'.format(pname, wpn.name))
cprint('While walking, you find a {}. It has a cute pink collar.'.format(doggy.name), attrs=['bold'])

functions.dacts('HIT, AVOID, EXAMINATE, STATS, EXIT')

while True:
	choice1 = functions.plinput()
	error = False
	if choice1.lower().startswith('hit'):
		if choice1.lower() == 'hit tame dog':
			doggy.ghit(wpn.attkm, wpn.attks)
			pass
		elif choice1.lower() == 'hit':
			cprint('\nYou must specify who to hit.', 'red', attrs=['bold'])
			error = True
			pass
		else:
			cprint('\nI did not get whoever you were trying to hit.', 'red', attrs=['bold'])
			error = True
			pass
	elif choice1.lower().startswith('avoid'):
		chance = functions.borg('You successfully avoided the {}!'.format(doggy.name), 'The {} blocked the path.'.format(doggy.name))
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
	elif choice1.lower().startswith('stats'):
		if choice1.lower() == 'stats me':
			print(statsl1 + pname)
			print(statsl2)
			print(statsl3)
			print(statsl4)
		elif choice1.lower() == 'stats tame dog':
			print(colored('\nHP: ', attrs=['bold']) + str(doggy.hp))
	elif choice1.lower().startswith('exit'):
		cprint('\nYou exited.', 'red', attrs=['bold'])
		os.system('cls')
		exit()
	else:
		cprint('\nSorry, but I didn\'t understand you.', 'red', attrs=['bold'])
		error = True
		pass
	if doggy.state == 'dead':
		break
	if error == True:
		continue
	turn = functions.borg('> The dog purrs.', '> The dog mooes violently!')

if doggy.state == 'dead':
	cprint('\nYou can either continue or examinate the dead body.', attrs=['bold'])
elif doggy.state == 'alive':
	cprint('You can either continue or examinate the Tame Dog.')
functions.dacts('EXAMINATE, CONTINUE, EXIT')
while True:
	choice2 = str(functions.plinput())
	error = False
	if choice2.lower().startswith('examinate'):
		if choice2.lower() == 'examinate tame dog':
			doggy.shstate()
			pass
		elif choice2.lower() == 'examinate':
			cprint('\nYou must specify what to examinate.', 'red', attrs=['bold'])
			error = True
			pass
	elif choice2.lower() == 'continue':
		break
	elif choice2.lower() == 'exit':
		cprint('\nYou exited.', 'red', attrs=['bold'])
		os.system('cls')
		exit()
	else:
		cprint('\nSorry, but I didn\'t understand you.', 'red', attrs=['bold'])
		pass
	if error == True:
		continue

neighbour = classes.Enemy('Happy Neighbour', 'A happy looking neighbour', 40, 'alive')
if doggy.state == 'dead':
	neighdiag1 = 'why did you kill a tame dog'
	neighdiag2 = 'really pissed off due to his dog being killed by you'
elif doggy.state == 'alive':
	neighdiag1 = 'how cute that dog was'
	neighdiag2 = 'blocking the path, saying you should go home'

cprint('\nYou continue your adventure, thinking about {}. While walking, you encounter your neighbour, who\'s {}.'.format(neighdiag1, neighdiag2), attrs=['bold'])

functions.dacts('HIT, AVOID, EXAMINATE, STATS, EXIT')

while True:
	choice1 = functions.plinput()
	error = False
	if choice1.lower().startswith('hit'):
		if choice1.lower() == 'hit happy neighbour':
			neighbour.ghit(wpn.attkm, wpn.attks)
			pass
		elif choice1.lower() == 'hit':
			cprint('\nYou must specify who to hit.', 'red', attrs=['bold'])
			error = True
			pass
		else:
			cprint('\nI did not get whoever you were trying to hit.', 'red', attrs=['bold'])
			error = True
			pass
	elif choice1.lower().startswith('avoid'):
		chance = functions.borg('You successfully avoided the {}!'.format(neighbour.name), 'The {} blocked the path.'.format(neighbour.name))
		if chance == 1:
			break
		elif chance == 2:
			pass
	elif choice1.lower().startswith('examinate'):
		if choice1.lower() == 'examinate neighbour':
			neighbour.shstate()
			pass
		elif choice1.lower() == 'examinate':
			cprint('\nYou must specify what to examinate.', 'red', attrs=['bold'])
			error = True
			pass
		else:
			cprint('\nI did not get whatever you were trying to examinate.', 'red', attrs=['bold'])
			error = True
			pass
	elif choice1.lower().startswith('stats'):
		if choice1.lower() == 'stats me':
			print(statsl1 + pname)
			print(statsl2)
			print(statsl3)
			print(statsl4)
		elif choice1.lower() == 'stats tame dog':
			print(colored('\nHP: ', attrs=['bold']) + str(neighbour.hp))
	elif choice1.lower().startswith('exit'):
		cprint('\nYou exited.', 'red', attrs=['bold'])
		os.system('cls')
		exit()
	else:
		cprint('\nSorry, but I didn\'t understand you.', 'red', attrs=['bold'])
		error = True
		pass
	if neighbour.state == 'dead':
		break
	if error == True:
		continue
	turn = functions.borg('> The man smiles at you.', '> The man is very disappointed.')
