from math import gcd

# Morgan Nordberg

# Problem: implement a class for rational numbers using operator overloading

# Algorithm: standard rational arithmetic

# Time complexity: every operation is O(1), because it's just basic arithmetic

class Rational:
    def __init__(self, x, y):
        x = int(x)
        y = int(y)
        g = gcd(x,y)
        x //= g
        y //= g
        if y < 0:
            x,y = -x,-y
        self.x = int(x) 
        self.y = int(y) 
    
    def __str__(self):
        return f"{self.x} / {self.y}"
    
    def __add__(self, other):
        a = self.x * other.y + self.y * other.x
        b = self.y * other.y
        return Rational(a,b) 

    def __sub__(self, other):
        a = self.x * other.y - self.y * other.x 
        b = self.y * other.y
        return Rational(a,b)
    
    def __mul__(self, other):
        a = self.x * other.x
        b = self.y * other.y
        return Rational(a,b)
    
    def __truediv__(self, other):
        a = self.x * other.y
        b = self.y * other.x
        return Rational(a,b)

    def __eq__(self, other):
        return self.x * other.y == other.x * self.y

    def __ne__(self, other):
        return self.x * other.y != other.x * self.y

    def __lt__(self, other):
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        return self.x * other.y <= other.x * self.y

    def __gt__(self, other):
        return self.x * other.y > other.x * self.y

    def __ge__(self, other):
        return self.x * other.y >= other.x * self.y


if __name__ == "__main__":
    input = open(0).readlines()
    for l in input[1:]:
        x,y,op,x1,y1 = l.split()
        a = Rational(x,y)
        b = Rational(x1,y1)
        match op:
            case '+': print(a+b)
            case '-': print(a-b)
            case '*': print(a*b)
            case '/': print(a/b)
