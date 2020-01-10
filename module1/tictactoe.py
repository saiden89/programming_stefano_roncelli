import random
def board_manager():
	board = [[],[],[]]

def player_pick():
	goes_first = 0
	player_1_pick = random.randint(0,1000)
	player_2_pick = random.randint(0,1000)
	if player_1_pick > player_2_pick:
		goes_first = 1
	else:
		goes_first = 2
	return(goes_first)


def input_name():
	player_1_name = input('Enter your name:')
	return input_name



def main():
	board_manager()
main()

import sys
print(sys.version)
