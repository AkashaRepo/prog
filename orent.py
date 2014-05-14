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