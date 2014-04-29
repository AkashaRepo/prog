#this is a proof of concept game in which a character can walk around a set of rooms and look at things.

print "You are in an elivator, type LOOK at any time for more information." #this string is displayed at the start of the game.
room = 'elivator' #this variable stores the player's location.

while room == 'elivator': #the player can use the following commnds in this room
	command = raw_input("Enter comand, you can go NORTH. Type LOOK for more info.\n")
	command = command.lower() #The above line asks the player for imput, and this line makes it lowercase for simplicty
	if command=='north': #this command changes the room the player is in.
		print "You enter the Multivac IO room."
		room = 'io' 
	elif command=='look': #this command displays more info but does not change the room.
		print "You are in an old industrial elivator."
		print "The Multiac IO room lies through a door to the NORTH."
	else: print "Invalid command." #this displays an error message, because the room is still the same, they can enter more commands.
	
while room == 'io':
	command = raw_input("Enter comand, you can go NORTH or SOUTH. Type LOOK for more info.\n")
	command = command.lower()	
	if command=='north':
		print "You enter the Multivac controll unit room."
		room = 'controll'
	elif command=='south':
		print "You enter the elivator."
		room = 'elivator'
	elif command=='look':
		print "You are in the Input/output room for Multivac."
		print "The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles."
		print "The controll unit lies to the NORTH, an elivator lies to the SOUTH."
	else: print "Invalid command."
	
while room == 'controll':
	command = raw_input("Enter comand, you can go NORTH, SOUTH, EAST, or WEST. Type LOOK for more info.\n")
	command = command.lower()
	if command =='north':
		print "You enter the Multivac Logic unit room."
		room = 'logic'
	elif command == 'south':
		print "You enter the Multivac IO room."
		room = 'io'
	elif command == 'east':
		print "You enter the Data Memory room."
		room = 'data'
	elif command == 'west':
		print "You enter the Instruction Memory room."
		room = 'instruction'
	elif command =='look':
		print "You are in the heart of Multivac. The controll unit towers above you. A mass of cables snake"
		print "in all directions, to the NORTH they lead to the ALU room, to the SOUTH is the IO room,"
		print "and to the EAST and WEST the data and instruction memory rooms respectively"
	else: print "Invalid command."
	
while room == 'logic':
	command = raw_input("Enter comand, you can go SOUTH. Type LOOK for more info.\n")
	command = command.lower()	
	if command =='south':
		print "You enter the Multivac controll unit room."
		room = 'controll'
	elif command =='look':
		print "You are in Multivac's Logic room. At the far end of the room stands rows and rows of logic units."
		print "The controll unit stands in the room to the SOUTH."
	else: print "Invalid command."

while room == 'data

