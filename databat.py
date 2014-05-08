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
	location = room
	print room['look'] #displays the line in the look index of the room dictonary
	command = prompt() #Runs the command prompt, fucntion, which currently does nothing
	
def look(room): #this function is simmilar to the enter() function, but does not change the room, just display it's text.
	print room['look']
	command = prompt()

def prompt(): #this function gives the player a command prompt. NOTE, this function is legacy and should be swapped out for something better latter.
	command = raw_input("Enter comand:\n")
	command = command.lower() #The above line asks the player for imput, and this line makes it lowercase for simplicty
	if command == 'look':
		look(location)
	elif command == 'north' or 'south' or 'east' or 'west' or 'up' or 'down':
		go(command)
	elif command == 'quit':
		print "Goodbye."
		import sys
		exit(0)
	else:
		print "Invalid command."
		command = prompt()

def go(direction): 
	#this function is supposed to be called when the player specifies a direction as a command.
	#It is supposed to check the current room's exits
	if direction == #is on the list of exits
	return enter(room) #change the location to the room listed for that exit's key.
	else: #if the exit is not avalable, it informs the player and asks for another command.
		print "You can't go that way"
		command = prompt()
	
	
location = elivator
enter(elivator) #right now all this game does is put the player in the elivator, there are no commands that can be used yet
