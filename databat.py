#Database for the Second revision of the walking game
#Instead of while loops, rooms will be defined by dictonaries containing all the relivant information about the room
#While the player is in the room, the game will display that rooms discriptive text, and allow the player to exicute comands specific to that room.
#Rooms can be added and removed without changing the overall code.
#Idealy the room database will be in a seperate file from the game's engine.

elivator = {
	'look':"You are inside a rusty old industrial elivator.",
	'exits':{'up':'exit','north':'io'}
	}
io = {
	'look':"You are in the Input/Output room for Multivac. The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles.",
	'exits':{'south':'Elivator','north':'Control'}
	}
control = {
	'look':"You are in the heart of Multivac. The control unit towers above you. A mass of cables snake in all directions",
	'exits':{'north':'logic','south':'io','east':'data','west':'instruction'}
	}
logic = {
	'look':"You are in Multivac's Logic room. At the far end of the room a row of massive logic units.",
	'exits':{'north':'control'}
	}
data = {
	'look':"The eastern side of the bunker is a cast arcade lined with rows and rows of data memmory units.",
	'exits':{'west':'control'},
	}
instruction = {
	'look':"The western side of the bunker is a vast arcade lined with rows and rows of instruction memmory units.",
	'exits':{'east':'control'}
	}

def enter(location): #this function is used when the player enters a room, it changes the room variable to match the new room.
	global room 
	room = location 
	return look() #once this function is finished, the look funciton should run.
	
def look(): #this function is displayed after the player enters a room, or when they enter the look comand.
	global room
	print room['look']
	return prompt() #once the text is displayed, the game asks for another command.

def quit(): #this function causes the game to crash, ending it.
	print 'Goodbye.'
	pass #this is the only funciton that will not eventualy loop back to prompt, thus ending the game.

def prompt(): #this function gives the player a command prompt.
	global room
	command = raw_input("Enter comand:\n") #This line asks the player for imput.
	command = command.lower()  #this line makes the imput lowercase to prevent capitalization errors
	directions = ['north','south','east','west','up','down'] #a list of directions
	if command in directions:
		return go(command) #if the command is a direction, the go(direction) function will take over.
	elif command == 'look':
		return look() #if the command is look, the look() function will take over.
	elif command == 'quit':
		return quit() #if the command is quit, the quit() function will take over.
	else:
		print "Invalid command."
		return prompt() #if the command is not valid, the prompt()funciton will call itself and ask the player again.

def go(direction): #this function is called when the player specifies a direction as a command. THE BUG IS PROBABLY HERE
	global room
	if direction in room['exits']:	#Checks the list of possible exits from the room's dictonary to see if that direction is valid.
		return enter(room['exits'][direction]) #changes the room to the room listed for that exit's key. <BUG PROBABLY IN THIS LINE
	else: 
		print "You can't go that way."
		return prompt() #if the exit is unavalable, calls prompt() again to ask for another command.

enter(elivator) #This starts the game by placing the player in the elivator.
