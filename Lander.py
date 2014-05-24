#this is my attempt at cloning the classic lunar lander game in text.


gravity = 1.62449
altitude = 100
velocity = 0
fuel = 200
print "Retro-burn complete, prepare for landing"
print "ERROR! autopilot failure!"
print "Switching to Manual Throttle"
falling = True
game = True

while game == True:
	while falling == True:
		velocity += gravity
		altitude -= velocity
		print "altitude: %s Meters" %(altitude)
		print "velocity: %s M/S" %(velocity)
		print "%s Fuel Units remaining" %(fuel)
		
		if altitude >= 0:
			falling = False
		else:
			throttle = raw_input('Manual throttle, 1-10: ')
			if throttle >= 1  and throttle <= 10:
				velocity -= throttle
			else:
				print "ERROR! Throttle accepts numeric values between 1 and 10"
				throttle = 0

	if falling == False:
		if velocity <= 5:
			print "you impact the lunar surface at %s M/S and Die." %(velocity)
			game = False
		else:
			print "you touch down at %s M/S with  %s Units of fuel remaining." %(velocity, fuel)
			if fuel <= 100:
				print "Unfortunately you do not have enough fuel to return to orbit."
				print "You will be the first man to die on the Moon."
				game = False
			else: 
				print "Congratulations, you are the first man to walk on the Moon."
				game = False
if game == False:
	print "GAME OVER."
