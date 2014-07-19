#This program prints a hex grid of arbitrary size.
def promptX():
	x = raw_input('Enter X dimension: ')
	try:
		x= int(x)
	except:
		print "Invalid dimension"
		return promptX()
	x = x+1
	return x
def promptY():
	y = raw_input('Enter Y dimension: ')
	try:
		y= int(y)
	except:
		print "Invalid dimension"
		return promptY()
	y = y-1
	return y
x = promptX()
y = promptY()
print "Printing Hexagons."
top = " __   "
upA = "/%s\\" %('**')
upB = "/%s\__" %('**')
dnA = "\__/%s" %('**')
dnB = "\__/"
bot = "\__/  "
print top * (x/2) 
for i in range(y):
	print upB * ((x/2)-1) + upA
	print dnA * ((x/2)-1) + dnB
print upB * ((x/2)-1) + upA
print bot * ((x/2))
print "\nDone."