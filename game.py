import sys, errors

possibleChoice = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e')

def userMove(userChoice):
	possible = 0
	print("Test input")
	userChoice=raw_input("Choose your option: \n")
	
	for choice in possibleChoice:
		if possible == 0: 
			if choice == userChoice:
				possible = 1;
			else: #do nothing
				break
	if possible == 1:
		print("Action will do this")
		return userChoice
	else:
		errors.badChoice()
