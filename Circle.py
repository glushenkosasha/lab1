import math

class Circle:
    def __init__(self, r):
        assert r > 0, "Radius must be positive"
        self.r = r

    def length(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * (self.r ** 2)

    def __str__(self) -> str:
        return f"Circle: r={self.r}"

    circle1 = Circle(5)
    print(circle1)

    circle2 = Circle(-2)