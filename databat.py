#Database for the Second revision of the walking game
#Instead of while loops, rooms will be defined by dictonaries containing all the relivant information about the room
#While the player is in the room, the game will display that rooms discriptive text, and allow the player to exicute comands specific to that room.
#Rooms can be added and removed without changing the overall code.
#Idealy the room database will be in a seperate file from the game's engine.

rooms = {
	'elivator':{
		'look':"You are inside a rusty old industrial elivator.",
		'exits':{'U':'exit','N':'io'}
		'contents':[]
		}
	"io":{
		'look':"You are in the Input/Output room for Multivac. The floor is covered in reems of paper printouts, and hundreds of lights flash on various consoles.",
		'exits':{'S':'Elivator','N':'Control'}
		'contents':[]
		}
	'control':{
		'look':"You are in the heart of Multivac. The control unit towers above you. A mass of cables snake in all directions",
		'exits':{'N':'logic','S':'io','E':'data','W':'instruction'}
		'contents':[]
		}
	'logic':{
		'look':"You are in Multivac's Logic room. At the far end of the room a row of massive logic units.",
		'exits':{'S':'control'}
		'contents':[]	
		}
	'data':{
		'look':"The eastern side of the bunker is a cast arcade lined with rows and rows of data memmory units.",
		'exits':{'W':'control'},
		'contents':[]
		}
	'instruction':{
		'look':"The western side of the bunker is a vast arcade lined with rows and rows of instruction memmory units.",
		'exits':{'E':'control'}
		'contents':[]
		}
}