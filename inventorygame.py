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
    
    
    
inventory = []
prompt = ">"
room_inventory = []
reward = []
        
intro()

while True:     # inside are two loops that alternate depending on how many items are in inventory
    while len(inventory) < 2: # when the inventory is low this loop lets the player pick up new items
        next = raw_input(prompt)
        if "bowl" == next:
            print "you have picked up the bowl, and put it in your inventory"
            inventory.append(bowl)
        elif "paper" == next:
            print "you have picked up the paper and put it into your inventory"
            inventory.append(paper)
        elif "pencil" == next:
            print "you have picked up the pencil and put it in your inventory"
            inventory.append(pencil)
        elif "thread" == next:
            print "you have picked up the thread and put it in your inventory"
            inventory.append(thread)
        elif "needle" == next:
            print "you have picked up the needle and put it in your inventory"
            inventory.append(needle)
        elif "soap" == next:
            print "you have picked up the soap and put it in your inventory"
            inventory.append(soap)
        else:
            print "I don't understand %s" % next

  
    while len(inventory) == 2: # when the inventory is full this loop combines places new combined items in the room
        if sum(inventory) == 3:
            print "you used the pencil and paper in your inventory to make a drawing"
            inventory = []
            room_inventory.append("drawing")
        elif sum(inventory) == 30:
            print "you used the sewing needle and thread in your inventory to embroider your shirt"
            inventory = []
            room_inventory.append("patch")
        elif sum(inventory) == 150:
            print "you used the bowl and the soap in your inventory to make suds"
            inventory = []
            room_inventory.append("suds")
        elif sum(inventory) == 51:
            print "you stab the pencil into the soap to make a crude sundial"
            inventory = []
            room_inventory.append("sundial")
        elif sum(inventory) == 60:
            print "you use the needle to carve the soap in your inventory into a soap sculpture"
            inventory = []
            room_inventory.append("soap sculpture")
        elif sum(inventory) == 110:
            print "you place the needle in the bowl in your inventory to make a crude compass"
            inventory = []
            room_inventory.append("compass")
        elif sum(inventory) == 70:
            print "you use the tie the soap with the string in your inventory to make a deer scare"
            inventory = []
            room_inventory.append("deer scare")
        else:
            print "the items you've picked up can't be combined"
            inventory = []
    
    while len(room_inventory) == 2:
        if "drawing" in room_inventory and "soap sculpture" in room_inventory:
            reward.append("artist")
            print "Magnifique! You've achieved the reward: Artist"
            room_inventory = []
        elif "patch" in room_inventory and "suds" in room_inventory:
            reward.append("homemaker")
            print "Well darn my socks, you've achieved the reward: Homemaker"
            room_inventory = []
        elif "sundial" in room_inventory and "compass" in room_inventory:
            reward.append("survivalist")
            print "You're prepared for anything! You've achieved the reward: Survivalist"
            room_inventory = []
        elif "deer scare" in room_inventory and "soap sculpture" in room_inventory:
            reward.append("free thinker")
            print "Eureka! You've achieved the reward: Free Thinker"
        else:
            print "you've made some things, but they don't lead to anything more."
            print "we'll just get rid of them for you"
            room_inventory = []
