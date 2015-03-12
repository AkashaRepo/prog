class HexCell(object):
    """A cell on a hexagonal map"""
    def __init__(self, Y, X, symbol):
        """Creates the cell with specificed symbol at the specified cordinates."""
        self.Y = Y
        self.X = X
        self.base = symbol
        self.contents = [] #This list will hold objects in the cell or something.
        #TODO list of exits

class HexMap(object):
    """A hexagonal map"""
    def __init__(self, Y, X, symbol):
        """Creates a map with specified dimensions and blank tile symbol."""
        self.Y = Y
        self.X = X
        self.blank = symbol
        self.grid = []
        for y in range(0, self.Y):
            row = []
            for x in range(0, self.X):
                cell = HexCell(y,x,self.blank)
                row.append(cell)
            self.grid.append(row)
        self.drawMap()
    def drawMap(self):
        """Renders the map. Called when anything changes.
        TODO: REWRITE ENTIRELY"""
    for row, y in enumerate(self.grid):
            if row %2== 1:
                print "",
            for x in y:
                print x,
            print ""
    def drawSymbol(self, Y, X, symbol):
        """Places a symbol on the map at a given coordinate.
        CURRENTLY DEPRECEATED
        TODO: REWRITE ENTIRELY"""
        #self.grid[Y][X] = symbol
    def eraseSymbol(self, Y, X):
        """Removes a symbol from the map, replacing it with the blank tile symbol.
        CURRENTLY DEPRECEATED
        TODO: REWRITE ENTIRELY"""
        #self.grid[Y][X] = self.blank

class Actor(object):
    """A symbol on the map"""
    def __init__(self, place, Y, X, symbol):
        """Places the actor on a specified map at a specified coordinate.
        CURRENTLY DEPRECEATED
        TODO: REWRITE ENTIRELY"""
        self.Y = Y
        self.X = X
        self.place = place
        self.symbol = symbol
        self.place.drawSymbol(self.Y,self.X,self.symbol)
        self.place.drawMap()
    def move(self, direction):
        """TODO: movement methods."""
    def kill(self):
        """Removes the actor from the map.
        CURRENTLY DEPRECEATED
        TODO: REWRITE ENTIRELY"""
        self.place.eraseSymbol(self.Y,self.X)
        self.place.drawMap()

Themap = HexMap(10,10,'.')
