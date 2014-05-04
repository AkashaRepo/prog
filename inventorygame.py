# this is a stupid game for finding out how to make inventories work //
# map
# this is a room that can not be exited. on the floor are some items. all the player can do is pick up the items.
# they have a two item inventory. If they pick up two items that can be combined, the items automatically combine.

# items
# pencil, paper, needle, thread, bowl, soap

# 1. pencil + paper = drawing
# 2. needle + thread = shirt patch
# 3. bowl + soap = soap carving
# 4. needle + bowl = soap sculpture
# 5. soap + thread = deer scare
# 6. needle + bowl = compass
# 7. pencil + soap = sundial

#  exclusions
#  if soap is used to make suds then soap can no longer be used. Every other item can be used infinitely

#  bonus
# suds + shirt patch = homemaker reward
#  drawing + soap carving = artist reward
#  compass + sundial = survivalist reward
#  deer scare + compass = weirdo reward

#  end description

pencil = 1
paper = 2
needle = 10
thread = 20
soap = 50
bowl = 100


def intro():
    print "You are in an inescapable room"
    print "there are some items in front of you"
    print "a green pencil, a bowl with a bit of water in it, a sewing needle"
    print "a piece of paper, a bar of floral smelling soap, and a spool of heavy cotton thread."
    print "what will you do?"
    go_forth()
    

prompt = ">"
next = raw_input(prompt)
    
inventory = []
if len(inventory) > 2:
    del(inventory[-1:])
    
intro()

while True:
    if next == "bowl":
        print "you have picked up the bowl"
        inventory.append(bowl)
        return next
    elif "paper" == next:
        print "you have picked up the paper"
        inventory.append(paper)
        return next
    elif "pencil" == next:
        print "you have picked up the pencil"
        inventory.append(pencil)
        return next
    elif "thread" == next:
        print "you have picked up the thread"
        inventory.append(thread)
        return next
    elif "needle" == next:
        print "you have picked up the needle"
        inventory.append(needle)
        return next
    elif "soap" == next:
        print "you have picked up the soap"
        inventory.append(soap)
        return next
    else:
        print "I do not understand %s" % next
        return next
    
    
