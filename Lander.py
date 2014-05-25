#this is my attempt at cloning the classic lunar lander game in text.
from time import sleep

gravity = 1.62449 #Meters per second per second, The gravity of the moon.
altitude = 100 #Meters.
velocity = 0 #Meters per second.
fuel = 40 #The player's starting fuel.
bingo = fuel/2 #Half the player's starting fuel, required to return to orbit.

sleep(.5)
print "\nRetro-burn complete, prepare for landing"
sleep(.5)
print "ERROR! autopilot failure!"
sleep(.5)
print "Switching to Manual Throttle"
sleep(.5)
falling = True
game = True

while game == True:
	while falling == True: #these things happen each time the game loops around, until altitude reaches zero.
		velocity += gravity
		altitude -= velocity
		if altitude <= 0 : #if the altitude is less than or equal to zero, the player has either landed or crashed
			falling = False
			break
		else: #If the player is still falling, they receive a data readout.
			print "\naltitude: %s Meters" %(altitude)
			print "velocity: %s M/S" %(velocity)
			if fuel >= bingo:
				print "%s Fuel Units remaining" %(fuel)
			elif fuel <= 0:
				print "WARNING! MAIN ENGINE FLAMEOUT! FUEL DEPRIVED!"
			elif fuel <= bingo:
				print "WARNING! Bingo fuel, %s units remaining" %(fuel)
			throttle = raw_input("Manual throttle, 0-9: ") #After receiving the readout, the player is given control of the throttle.
			if len(throttle) <= 0: #if the player enters nothing, count it as if they had entered a value of 0
				throttle = 0
			else:
				throttle = throttle[0] #Strips all but the first character
				if throttle not in ('0123456789'): #If the player enters something invalid, return an error message and count it as if they had entered a value of 0
					print "ERROR! Throttle accepts numeric values between 0 and 9"
					throttle = 0
				else: #turns the numeric string into an int so the game can use it.
					throttle = int(throttle) 
					if throttle >= fuel: #If the player runs out of fuel, they can no longer use the throttle properly.
						throttle = fuel
					fuel -= throttle
					velocity -= throttle

	if falling == False: #These things happen once the player touches the ground
		if velocity >= 5.0 :
			print "\nyou impact the lunar surface at %s M/S and Die." %(velocity)
			game = False
		else:
			print "\nyou touch down at %s M/S with  %s Units of fuel remaining." %(velocity, fuel)
			if fuel <= bingo:
				sleep(.5)
				print "Unfortunately you do not have enough fuel to return to orbit."
				sleep(.5)
				print "You will be the first person to die on the Moon."
				game = False
			else: 
				sleep(.5)
				print "Congratulations, you are the first person to land on the Moon's surface."
				game = False
if game == False:
	sleep(.5)
	print "\nGAME OVER."