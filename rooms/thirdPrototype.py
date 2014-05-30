#There should be rooms
#The player should be able to move through rooms via exits linking rooms
#Rooms should have a description the player can read
#some of these rooms should have objects
#some objects should be unique, and others should have multiple identical copies.
#the player should have the ability to interact with objects
#some objects can be picked up, carried in inventory, and placed in different places
#some rooms and objects can interact with each other in arbitrary ways independent from the player

class HelloWorld:
	def __init__(self, msg):
		self.msg = msg

	def write(self):
		print self.msg

printer = HelloWorld("Hello, World!")
printer.write()

class room(object):
	"""This is a generic room"""
	def __init__(self, name, look, exits, contents, scripts):
		super(room, self).__init__()
		self.name = name
		self.look = look
		self.exits = exits
		self.contents = contents
		self.scripts = scripts
		assert type(self.name) is str
		assert type(self.look) is str
		assert type(self.exits) is dict
		assert type(self.contents) is list
		assert type(self.scripts) is list

		def enter(self):
			global room
			room = self
			return look(self)
		def look(self):
			print self.look
			pass

elevator = room(name='elevator',
				look="You You are inside a rusty old industrial elevator.",
				exits={'up':'outside','north':'io'} ,
				contents=[],
				scripts=[])

elevator.look()
