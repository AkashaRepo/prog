print "This is the elivator, type LOOK at any time for more information."
room = elivator

while room == elivator:
	command = raw_input("Enter comand, you can go NORTH")
	
	if command=='north':
		print "You enter the Multivac IO room."
		room = io
	if command=='look':
		print "You are in an old industrial elivator."
	else: print "Invalid command."
	
while room == io:
	command = raw_input("Enter comand, you can go NORTH or SOUTH")
	
	if command=='north':
		print "You enter the Multivac controll unit room."
		room = controll
	if command=='south':
		print "You enter the elivator."
		room = elivator
	if command=='look':
		print "You are in the Input/output room for Multivac."
	else: print "Invalid command."
	
while room == controll:
	
