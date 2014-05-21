class Table(object):
    def __init__(self, x): # x is the players, the sushi table, the beer.
        x = self.x  # constantly reloads everything?
        
class SushiDish(Table): # the sushi plate is on the table
    def __init__(self, sushi_order, sushi_piece):  # can sushi_piece be defined here? the sushi_order is the type of sushi
        sushi_order = self.sushi_order # should contain the time the sushi takes to eat.
    
class Player(Table): # contains stored points of player 1 and player 2
    def __init__(self, player): # player is either player 1 or 2
        self.player = player
   
class Beer(Table): # contains the beer
    def __init__(self, drink): # drink is the individual beer
        self.drink = drink
   
class VeggieRoll(SushiDish): # contains three pieces of veggie roll, the points gained for each
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece
        
class ShrimpRoll(SushiDish): #contains pieces of sushi, + point value
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece
    
class TunaRoll(SushiDish):
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece
    
class Edamame(SushiDish):
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece # sushi_piece contains the time the food takes to eat (but this is the same for all sushi?) and the points you recieve once finished eating
