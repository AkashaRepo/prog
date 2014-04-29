print "This is the elivator, type LOOK at any time for more information."
room = elivator

while room == elivator:
	command = raw_input("Enter comand, you can go NORTH")
	
	if command=='north':
		print "You enter the Multivac IO room."
		room = io
	elif command=='look':
		print "You are in an old industrial elivator."
		print "The Multiac IO room lies through a door to the NORTH."
	else: print "Invalid command."
	
while room == io:
	command = raw_input("Enter comand, you can go NORTH or SOUTH")
	
	if command=='north':
		print "You enter the Multivac controll unit room."
		room = controll
	elif command=='south':
		print "You enter the elivator."
		room = elivator
	elif command=='look':
		print "You are in the Input/output room for Multivac."
		print "The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles."
		print "The controll unit lies to the NORTH, an elivator lies to the SOUTH."
	else: print "Invalid command."
	
while room == controll:
	command = raw_input("Enter comand, you can go NORTH, SOUTH, EAST, or WEST")
	
	if command=='north':
		print "You enter the Multivac Logic unit room."
		room = logic
	elif command == 'south':
		print "You enter the Multivac IO room."
		room = io
	elif command == 'east':
		print "You enter the Data Memory room."
		room = data
	elif command == 'west':
		print "You enter the Instruction Memory room."
		room = instruction
	elif command =='look':
		print "You are in the heart of Multivac. The controll unit towers above you. A mass of cables snake"
		print "in all directions, to the NORTH they lead to the ALU room, to the SOUTH is the IO room,"
		print "and to the EAST and WEST the data and instruction memory rooms respectively"
	else: print "Invalid command."


