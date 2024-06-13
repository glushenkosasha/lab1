class Trapeze:
    def __init__(self, a, b, c, d, height):
        assert a > 0 and b > 0 and c > 0 and d > 0 and a + b > c and a + b > d and a != b
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height


    def perimeter(self):
        res = (self.a + self.b + self.c + self.d)
        return res

    def area(self):
        res = ((self.b + self.d) / 2) * self.height
        return res

        if isinstance(res, complex):

            res_list = [round(res.real, 2), round(res.imag, 2)]
            ressy = max(result_list)
            return ressy
        else:

            return round(res, 2)



    def __str__(self) -> str:
        return f"Trapeze: a={self.a} b={self.b} c={self.c} d={self.d}"