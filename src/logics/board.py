
class Board:

    def __init__(self, owner):
        self.owner = owner
        
        self.width = 4
        self.height = 2

        self.array = [None] * (self.width * self.height)
    
    def get(self, x, y):
        return self.array[ convert_2d_to_1d(self.width, x, y) ]
    def set(self, x, y, val):
        self.array[ convert_2d_to_1d(self.width, x, y) ] = val


def convert_2d_to_1d(width, x, y):
    return y * width + x
def convert_1d_to_2d(width, index):
    return (index % width, int(index / width))


