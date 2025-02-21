# area of the square 
def Square(a):
    area = a*a
    print(f"Area of the square with side {a} is {area}")

def Rectangle(a,b):
    area = a*b
    print(f"Area of the rectangle with sides  {a} and {b} is {area}")

def Circle(r):
    area= 3.14*r*r
    print(f"Area of the circle with radius {r} is {area}")

def Triangle(b,h):
    area= int((b*h)/2)
    print(f"Area of the triangle with height {h} and base {b} is {area}")

Square(4)
Rectangle(3,5)
Circle(3)
Triangle(4,5)