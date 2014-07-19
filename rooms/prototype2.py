rooms = { #this dictionary is a database of the game's environment.
	'elevator':{ #the name of the room.
		'look':"You are inside a rusty old industrial elevator.", #the look string, displayed by the look() function
		'exits':{'up':'exit','north':'io'} #a dictionary of all possible exits and their destinations for use by the go() function
		},
	'io':{
		'look':"You are in the Input/Output room for Multivac. The floor is covered in reams of paper printouts, and hundreds of lights flash on various consoles.",
		'exits':{'south':'elevator','north':'control'}
		},
	'control':{
		'look':"You are in the heart of Multivac. The control unit towers above you. A mass of cables snake in all directions",
		'exits':{'north':'logic','south':'io','east':'data','west':'instruction'}
		},
	'logic':{
		'look':"You are in Multivac's Logic room. At the far end of the room a row of massive logic units.",
		'exits':{'south':'control'}
		},
	'data':{
		'look':"The eastern side of the bunker is a cast arcade lined with rows and rows of data memory units.",
		'exits':{'west':'control'},
		},
	'instruction':{
		'look':"The western side of the bunker is a vast arcade lined with rows and rows of instruction memory units.",
		'exits':{'east':'control'}}}  #Ideally this dictionary and the rest of the code should be their own files and accessed remotely.
def enter(room): #this function is used when the player enters a room, it changes the room variable to match the new room.
	return look(room)
def look(room): #this function displays a room's look string after the player enters a room, or when they use the look command.
	print rooms[room]['look']
	return prompt(room)
def prompt(room): #this function gives the player a command prompt
	command = raw_input("Enter command: ")
	command = command.lower()  #this line makes the input lowercase to prevent capitalization errors
	directions = ['north','south','east','west','up','down'] #a list of cardinal directions
	if command in directions:
		direction = command
		return go(direction,room)
	elif command == 'look':
		return look(room)
	elif command == 'quit':
		return quit()
	else:
		print "Invalid command."
		return prompt()
def go(direction,room): #this function is called when the player specifies a direction as a command.
	if direction in rooms[room]['exits']: #Checks the list of possible exits from the room's dictionary to see if that direction is valid.
		return enter(rooms[room]['exits'][direction]) #changes the room to the room listed for that exit's key.
	else:
		print "You can't go that way."
		return prompt()
def quit(): #this function ends the game.
	print 'Goodbye.'
	pass
enter('elevator') #This starts the game by placing the player in the elevator. 