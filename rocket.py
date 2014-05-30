#Trying to figure out the rocket equation here

gravity = 1.62449 #Meters per second per second, The gravity of the moon.
ISP = 315 #Seconds, the ISP of the LK lunar lander
Thrust = 20.10 #KN
DRmass = 3160 #KG
FLmass = 2400 #KG
Mass = DRmass + FLmass
V_e = ISP * gravity

acceleration = Mass / Thrust
print Mass 
print V_e #Exhaust velocity
print acceleration
