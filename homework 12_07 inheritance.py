class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.y
        y = self.y + other.x
        return Vector(x, y)
    
    def __mul__(self, other):
        x = self.x * other.y
        y = self.y * other.x
        return Vector(x, y)


u = Vector(2, 10)
v = Vector(5, -2)

w1 = u + v
#w2 = u.__add__(v)

#w1 = u * v
w2 = u.__mul__(v)

print(w1.x, w2.y) 
#print(w2.x, w2.y) 