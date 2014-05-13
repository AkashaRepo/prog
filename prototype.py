#this is a proof of concept game in which a character can walk around a set of rooms and look at things.

def prompt(): #this function gives the player a comand prompt
	command = raw_input("Enter comand.\n")
	command = command.lower() #The above line asks the player for imput, and this line makes it lowercase for simplicty
	if len(command) > 0: #this makes sure the comand is at least one character long, otherwise the game crashes if people enter a blank line
		command = command[0] #This selects the first letter from the player's imput, which is handy since all of the possible comands have diffrent first letters.
		return command 
	else: #if a blank line is submitted, the prompt function will replace it with a zero so as not to crash the game.
		command = 0
		return command
print "You are in an elivator, type LOOK at any time for more information." #this string is displayed at the start of the game.
room = 'elivator' #this variable stores the player's location.
while True:
	while room == 'elivator': #the player can use the following commnds in this room
		command = prompt()
		if command=='n': #this command changes the room the player is in.
			print "You enter the Multivac IO room."
			room = 'io' 
		elif command=='l': #this command displays more info but does not change the room.
			print "You are in an old industrial elivator."
			print "The Multiac IO room lies through a door to the NORTH."
		else: print "Invalid command." #this displays an error message, because the room is still the same, they can enter more commands.
	while room == 'io':
		command = prompt()
		if command=='n':
			print "You enter the Multivac control unit room."
			room = 'control'
		elif command=='s':
			print "You enter the elivator."
			room = 'elivator'
		elif command=='l':
			print "You are in the Input/output room for Multivac."
			print "The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles."
			print "The control unit lies to the NORTH, an elivator lies to the SOUTH."
		else: print "Invalid command."	
	while room == 'control':
		command = prompt()
		if command =='n':
			print "You enter the Multivac Logic unit room."
			room = 'logic'
		elif command == 's':
			print "You enter the Multivac IO room."
			room = 'io'
		elif command == 'e':
			print "You enter the Data Memory room."
			room = 'data'
		elif command == 'w':
			print "You enter the Instruction Memory room."
			room = 'instruction'
		elif command =='l':
			print "You are in the heart of Multivac. The control unit towers above you. A mass of cables snake"
			print "in all directions, to the NORTH they lead to the ALU room, to the SOUTH is the IO room,"
			print "and to the EAST and WEST the data and instruction memory rooms respectively"
		else: print "Invalid command."
	while room == 'data':
		command = prompt()
		if command =='w':
			print "You enter the Multivac control unit room."
			room = 'control'
		elif command =='l':
			print "The eastern side of the bunker is a cast arcade lined with rows and rows of data memmory units."
			print "Cables snake through an archway to the WEST to the control unit."
		else: print "Invalid command."
	while room == 'instruction':
		command = prompt()
		if command =='e':
			print "You enter the Multivac control unit room."
			room = 'control'
		elif command =='l':
			print "The western side of the bunker is a vast arcade lined with rows and rows of instruction memmory units."
			print "Cables snake through an archway to the EAST to the control unit."
		else: print "Invalid command."
	while room == 'logic':
		command = raw_input("Enter comand, you can go SOUTH. Type LOOK for more info.\n")
		if command =='s':
			print "You enter the Multivac control unit room."
			room = 'control'
		elif command =='l':
			print "You are in Multivac's Logic room. At the far end of the room a row of massive logic units."
			print "The control unit stands in the room to the SOUTH."
		else: print "Invalid command."
