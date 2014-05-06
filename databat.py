#Database for the Second revision of the walking game
#Instead of while loops, rooms will be defined by dictonaries containing all the relivant information about the room
#While the player is in the room, the game will display that rooms discriptive text, and allow the player to exicute comands specific to that room.
#Rooms can be added and removed without changing the overall code.
#Idealy the room database will be in a seperate file from the game's engine.

Elivator = {
	'look':"You are inside a rusty old industrial elivator.",
	'exits': {'U':'exit','N':'IO'}
	}
IO = {
	'look':"You are in the Input/output room for Multivac. The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles.",
	'exits':{'S':'Elivator','N':'Control'}
	}
