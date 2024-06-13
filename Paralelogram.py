class Parallelogram:
    def __init__(self, a, b, h):
        assert a > 0 and b > 0 and h > 0 and a > h and b > h
        self.a = a
        self.b = b
        self.height = height

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def __str__(self) -> str:
        return f"paralelogram: a={self.a} b={self.b} h={self.h}"