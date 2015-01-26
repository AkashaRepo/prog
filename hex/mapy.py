class HexMap(object):
    """A hexagonal map"""
    def __init__(self, Y, X, symbol):
        """initalizes the map dimensions and blank tile symbol."""
        self.Ysize = Y
        self.Xsize = X
        self.blank = symbol
        self.grid = []
        for y in range (0, self.Ysize):
            row = []
            for x in range (0, self.Xsize):
                row.append(self.blank)
            self.grid.append(row)
    def drawMap(self):
        """Renders the map. Should be called when anything changes."""
        for row, y in enumerate(self.grid):
            if row %2== 1:
                print "",
            for x in y:
                print x,
            print ""

Newmap = HexMap(10,10,'.')
Newmap.drawMap()
