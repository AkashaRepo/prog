#This program prints a hexagonal grid of arbitrary size 
def promptX(): #Prompts the user for an X dimension, Right now only odd numbers work properly, evens get rounded down 
	x = raw_input('Enter X dimension: ')
	try:
		x= int(x)
	except:
		print "Invalid dimension"
		return promptX()
	if x < 1:
		print "Invalid dimension"
		return promptX()
	x = x+1
	return x

def promptY():#Prompts the user for a Y dimension 
	y = raw_input('Enter Y dimension: ')
	try:
		y= int(y)
	except:
		print "Invalid dimension"
		return promptY()
	if y < 1:
		print "Invalid dimension"
		return promptY()
	y = y-1
	return y

def promptSize(): #Prompts the user for a hexagon size
	size = raw_input('Enter Hexagon size 1-2: ')
	if size == '1':
		return printhex(1)
	if size == '2':
		return printhex(2)
	else:
		print "Invalid size"
		return promptSize()

def printhex(size):#Prints the hexagons
	print "Printing Hexagons,"
	if size == 1: # for hexagons of size 1
		Top = " __   "
		TopEnd = " __"
		Up = "/  \__"
		UpEnd = "/  \\"
		Down = "\__/"
		DownEnd = "\__/  "
		Bottom = "\__/  "
		BottomEnd ="\__/"
		print Top * ((x/2)-1) + TopEnd
		for i in range(y):
			print Up * ((x/2)-1) + UpEnd
			print DownEnd * ((x/2)-1) + Down
		print Up * ((x/2)-1) + UpEnd
		print Bottom * ((x/2)-1) + BottomEnd
	elif size == 2: # for hexagons of size 2, size 2 hexes currently has a min Y dimension of 2
		Top3 = "  ____      "
		Top3End = "  ____"
		Top2 = "/    \\      "
		Top2End = "/    \\"
		Up2 = "/    \\      "
		Up2End = "/    \\"
		Up1 = "/      \\____"
		Up1End = "/      \\"
		Down1 = "\\      /    "
		Down1End = "\\      /"
		Down2 = "\\____/      "
		Down2End = "\\____/"
		Bottom1 = "\\      /    "
		Bottom1End = "\\      /"
		Bottom2 = "\\____/      "
		Bottom2End = "\\____/"
		print Top3 * ((x/2)-1) + Top3End
		print ' ' + Top2 * ((x/2)-1) + Top2End
		print Up1 * ((x/2)-1) + Up1End
		print Down1 * ((x/2)-1) + Down1End
		print " " + Down2 * ((x/2)-1) + Down2End
		for i in range(y):
			print ' ' + Up2 * ((x/2)-1) + Up2End
			print Up1 * ((x/2)-1) + Up1End
			print Down1 * ((x/2)-1) + Down1End
			print ' ' + Down2 * ((x/2)-1) + Down2End
		print ' ' + Up2 * ((x/2)-1) + Up2End
		print Up1 * ((x/2)-1) + Up1End
		print Bottom1 * ((x/2)-1) + Bottom1End
		print " " + Bottom2 * ((x/2)-1) + Bottom2End

#Program starts here 
print "H E X A G O N\n P R I N T E R"
x = promptX()
y = promptY()
size = promptSize()
print "\nDone!"