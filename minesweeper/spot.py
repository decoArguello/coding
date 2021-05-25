

class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isMine = False
        self.isFlagged = False
        self.isDiscovered = False
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_is_flagged(self):
        return self.isFlagged
    
    def get_is_discovered(self):
        return self.isDiscovered

    def get_is_mine(self):
        return self.isMine
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.x = y
    
    def set_is_discovered(self, isDiscovered):
        self.isDiscovered = isDiscovered
    
    def set_is_mine(self, isMine):
        self.isMine = isMine
    
    def set_is_flagged(self, isFlagged):
        self.isFlagged = isFlagged
    