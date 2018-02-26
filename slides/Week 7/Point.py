class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def copy(self):
        newPoint = Point(self.x, self.y)

        return newPoint

a = Point(5,4)
b = Point(3,2)

b = a.copy()

b.x = 7

print(str(a.x) + ", " + str(a.y))
print(str(b.x) + ", " + str(b.y))
