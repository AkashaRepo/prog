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

items = ["paper", "pencil", "needle", "thread", "soap", "bowl"]
prizes = ["Artist", "Survivalist", "Homemaker", "Free Thinker"]

def intro():
    print "You are in an inescapable room"
    print "there are some items in front of you"
    for x in items:
        if x not in inventory:
            print x
    print "what will you do?"
    
    
game = True    
inventory = [] # there can only be two items in inventory
prompt = ">"
room_inventory = [] # there are items you make that go on the floor.
reward = [] # there are four rewards. If you collect them all, you win!
        
intro() # game begins

while game == True:     # inside are loops that alternate depending on how many items are in inventory
    while len(inventory) < 2: # when the inventory is low this loop lets the player pick up new items
        next = raw_input(prompt)
        if 'look' == next:
            intro()
            if len(inventory) > 0:
                print "inventory:"
                print inventory
        elif "bowl" == next:
            print "You have picked up the bowl."
            inventory.append("bowl")
        elif "paper" == next:
            print "You have picked up the paper."
            inventory.append("paper")
        elif "pencil" == next:
            print "You have picked up the pencil."
            inventory.append("pencil")
        elif "thread" == next:
            print "You have picked up the thread."
            inventory.append("thread")
        elif "needle" == next:
            print "you have picked up the needle."
            inventory.append("needle")
        elif "soap" == next:
            print "You have picked up the soap."
            inventory.append("soap")
        else:
            print "I don't understand %s" % next

  
    while len(inventory) == 2:# when the inventory is full this loop combines places new combined items in the room
        print "you have the %s and the %s in your inventory" % (inventory[0], inventory[1])
        if "pencil" in inventory and "paper" in inventory:
            print "You used the pencil and paper to make a drawing."
            print "You put the drawing on the floor and empty your inventory."
            inventory = []
            room_inventory.append("drawing")
        elif "thread" in inventory and "needle" in inventory:
            print "you used the sewing needle and thread to embroider your shirt"
            print "you return the needle and thread to the floor"
            inventory = []
            room_inventory.append("patch")
        elif "soap" in inventory and "bowl" in inventory:
            print "you used the bowl and the soap to make suds"
            print "you scrub the floor with the suds and empty your inventory."
            inventory = []
            room_inventory.append("suds")
        elif "pencil" in inventory and "soap" in inventory:
            print "You stab the pencil into the soap to make a crude sundial"
            print "You set the sundial on the floor. There's no natural light here but it's nice anyway."
            print "You empty your inventory."
            inventory = []
            room_inventory.append("sundial")
        elif "needle" in inventory and "soap" in inventory:
            print "You use the needle to carve the soap into a soap sculpture."
            print "You set the sculpture on the floor and empty your inventory."
            inventory = []
            room_inventory.append("soap sculpture")
        elif "needle" in inventory and "bowl" in inventory:
            print "You place the needle in the bowl to make a crude compass."
            print 'You put the compass on the floor and empty your inventory.'
            inventory = []
            room_inventory.append("compass")
        elif 'soap' in inventory and "thread" in inventory:
            print "You tie the soap up with the thread to make a deer scare."
            print "You set the deer scare on the floor and empty your inventory."
            inventory = []
            room_inventory.append("deer scare")
        else:
            print "The items you've picked up can't be combined, so you put them back on the floor."
            inventory = []
    
    while len(room_inventory) == 2:
        if "drawing" in room_inventory and "soap sculpture" in room_inventory:
            reward.append("artist")
            print "Magnifique! You've made a drawing and a soap sculpture,"
            print "and achieved the reward: Artist"
            room_inventory = []
        elif "patch" in room_inventory and "suds" in room_inventory:
            reward.append("homemaker")
            print "Well darn my socks, you've cleaned the floor and mended your shirt,"
            print "and you've achieved the reward: Homemaker"
            room_inventory = []
        elif "sundial" in room_inventory and "compass" in room_inventory:
            reward.append("survivalist")
            print "You're prepared for anything! You made survival tools out of these" 
            print "spare materials and you've achieved the reward: Survivalist"
            room_inventory = []
        elif "deer scare" in room_inventory and "soap sculpture" in room_inventory:
            reward.append("free thinker")
            print "Eureka! You combined things in odd ways and"
            print "you've achieved the reward: Free Thinker"
            room_inventory = []
        else:
            print "You've made some things, but the floor is getting quite cluttered."
            print "We'll just clear the floor for you."
            room_inventory = []
            
    if len(reward) == 1:
        print "You've got one reward, maybe there are more..."
    
        
    if len(reward) == 2:
        if reward[1] == reward[0]:
            del(reward[1])
        else:
            print "You've got two rewards, maybe there are more..."
        
        
    if len(reward) == 3:
        if reward[1] == reward[2] or reward[0] == reward[2]:
            del(reward[2])
        else:
            print "You've got three rewards, getting close now..."
        
            
    if len(reward) == 4:
        if reward[3] == reward[2] or reward[3] == reward[1] or reward[3] == reward[0]:
            del(reward[3])
            print "You got the same reward more than once, we fixed that for you by deleting the extras."
        else:
            print "Great Job, you got all four rewards and won the game!"
            game = False
            break
        
