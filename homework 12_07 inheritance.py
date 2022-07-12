class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.y
        y = self.y + other.x
        return Number(x, y)
    
    def __mul__(self, other):
        x = self.x * other.y
        y = self.y * other.x
        return Number(x, y)


u = Number(2, 10)
v = Number(5, -2)

#w1 = u + v
w1 = u.__add__(v)

#w2 = u * v
w2 = u.__mul__(v)

print(w1.x, w2.y) 
