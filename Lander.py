#this is my attempt at cloning the classic lunar lander game in text.


gravity = 1.62449 #The gravity of the moon.
altitude = 100 #The player's starting altitude.
velocity = 0 #The player's starting velocity
fuel = 40 #The player's starting fuel
bingo = fuel/2
print "Retro-burn complete, prepare for landing"
print "ERROR! autopilot failure!"
print "Switching to Manual Throttle"
falling = True
game = True

while game == True:
	while falling == True: #these things happen each time the game loops around, until altitude reaches zero.
		velocity += gravity
		altitude -= velocity
		print "\naltitude: %s Meters" %(altitude)
		print "velocity: %s M/S" %(velocity)
		if fuel >= bingo:
			print "%s Fuel Units remaining" %(fuel)
		elif fuel <= bingo:
			print "WARNING! Bingo fuel, %s units remaining" %(fuel)
		elif fuel <= 0:
			print "WARNING! MAIN ENGINE FLAMEOUT! FUEL DEPRIVED!"
		
		if altitude <= 0 : #if the altitude is less than or equal to zero, the player has either landed or crashed
			falling = False
		else: #If the spacecraft is falling, the player is asked for a number between 0 and 9
			throttle = raw_input("Manual throttle, 0-9: ")
			if len(throttle) <= 0:
				throttle = 0
			else:
				throttle = throttle[0] #Strips all but the first character
				if throttle not in ('0123456789'): #makes sure that character is a digit
					print "ERROR! Throttle accepts numeric values between 0 and 9"
					throttle = 0
				else:
					throttle = int(throttle)
					if throttle >= fuel:
						throttle = fuel
					fuel -= throttle
					velocity -= throttle

	if falling == False:
		if velocity >= 5.0 :
			print "you impact the lunar surface at %s M/S and Die." %(velocity)
			game = False
		else:
			print "you touch down at %s M/S with  %s Units of fuel remaining." %(velocity, fuel)
			if fuel <= bingo:
				print "Unfortunately you do not have enough fuel to return to orbit."
				print "You will be the first person to die on the Moon."
				game = False
			else: 
				print "Congratulations, you are the first person to walk on the Moon."
				game = False
if game == False:
	print "GAME OVER."