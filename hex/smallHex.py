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
print "Done"
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


#print "  P L A N E T A R Y         __ "
#print "   H E X     M A P         /NP\ "
#print "    __    __    __    __   \__/ "
#print " __/N1\__/N3\__/N5\__/N7\__/N9\ "
#print "/N0\__/N2\__/N4\__/N6\__/N8\__/ "
#print "\__/E1\__/E3\__/E5\__/E7\__/E9\ "
#print "/E0\__/E2\__/E4\__/E6\__/E8\__/ "
#print "\__/S1\__/S3\__/S5\__/S7\__/S9\ "
#print "/S0\__/S2\__/S4\__/S6\__/S8\__/ "
#print "\__/  \__/  \__/  \__/  \__/ " 
#print "                        /SP\ "
#print " S U B   H E X   M A P  \__/ "
#print " __    __    __    __    __ "
#print "/  \__/\_\__/__\__/_/\__/  \ "
#print "\__/  \/_/  \__/  \_\/  \__/ "
#print "/  \__/  \__/  \__/  \__/  \ "
#print "\__/ /\__/  \__/  \__/\ \__/ "
#print "/  \/_/  \__/  \__/  \_\/  \ "
#print "\__/  \__/  \__/  \__/  \__/ "
#print "/_/\__/  \__/00\__/  \__/\_\ "
#print "\_\/  \__/  \__/  \__/  \/ / "
#print "/  \__/  \__/  \__/  \__/  \ "
#print "\__/\ \__/  \__/  \__/ /\__/ "
#print "/  \_\/  \__/  \__/  \/_/  \ "
#print "\__/  \__/  \__/  \__/  \__/ "
#print "/  \__/\_\__/__\__/_/\__/  \ "
#print "\__/  \/_/  \__/  \_\/  \__/ "