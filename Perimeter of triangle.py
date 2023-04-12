class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        result = self.a + self.b + self.c
        return result
    
triangle1 = Triangle(3,4,5)
perimeter_result = triangle1.perimeter()
print("Perimeter of Triangle 1:", perimeter_result)