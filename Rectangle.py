class Rectangle:
    def __init__(self, a, b):
        assert a > 0 and b > 0
        self.a = a
        self.b = b


    def perimeter(self):
        return (2 * self.a + 2 * self.b)

    def area(self):
       return (self.a * self.b)

    def __str__(self) -> str:
        return f"Rectangle: a={self.a} b={self.b}"