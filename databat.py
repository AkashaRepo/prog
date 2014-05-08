#Database for the Second revision of the walking game
#Instead of while loops, rooms will be defined by dictonaries containing all the relivant information about the room
#While the player is in the room, the game will display that rooms discriptive text, and allow the player to exicute comands specific to that room.
#Rooms can be added and removed without changing the overall code.
#Idealy the room database will be in a seperate file from the game's engine.

elivator = {
	'look':"You are inside a rusty old industrial elivator.",
	'exits':{'U':'exit','N':'io'}
	}
io = {
	'look':"You are in the Input/Output room for Multivac. The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles.",
	'exits':{'S':'Elivator','N':'Control'}
	}
control = {
	'look':"You are in the heart of Multivac. The control unit towers above you. A mass of cables snake in all directions",
	'exits':{'N':'logic','S':'io','E':'data','W':'instruction'}
	}
logic = {
	'look':"You are in Multivac's Logic room. At the far end of the room a row of massive logic units.",
	'exits':{'S':'control'}
	}
data = {
	'look':"The eastern side of the bunker is a cast arcade lined with rows and rows of data memmory units.",
	'exits':{'W':'control'},
	}
instruction = {
	'look':"The western side of the bunker is a vast arcade lined with rows and rows of instruction memmory units.",
	'exits':{'E':'control'}
	}

#while the game is running, check which room the player is in. Display that room's 'look' string then ask them for a command.
#usualy this command will be a direction, if that command is on that room's dictonary of exits, change the room to the one on that exit's index. Then start this process over in the new room.

def enter(room): #this function is used when the player enters a room, or types look.
	print room['look'] #displays the line in the look index of the room dictonary
	command = prompt() #asks the player for a command using the prompt() function
	if command == 'n':
		pass #check to see if there is an 'n' exit, and then go there
	elif command == 's':
		pass
	elif command == 'e':
		pass
	elif command == 'w':
		pass
	elif command == 'l':
		enter(room)
	else:
		pass

def prompt(): #this function gives the player a command prompt. NOTE, this function is legacy and should be swapped out for something better latter.
	command = raw_input("Enter comand.\n")
	command = command.lower() #The above line asks the player for imput, and this line makes it lowercase for simplicty
	if len(command) > 0: #this makes sure the comand is at least one character long, otherwise the game crashes if people enter a blank line
		command = command[0] #This selects the first letter from the player's imput, which is handy since all of the possible comands have diffrent first letters.
		return command 
	else: #if a blank line is submitted, the prompt function will replace it with a zero so as not to crash the game.
		command = 0
		return command

enter(elivator)