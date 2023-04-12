class Polygon:
    def __init__(self, sides):
        self.sides = sides
        
    def display_info(self):
        print("A Polygon is a two dimensional shape with straight lines")
        
    def get_perimeter(self):
        result = sum(self.sides)
        return result
    
class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a Polygon with three sides")
        
class Quadrilateral(Polygon):
    def display_info(self):
        print("A Quadrilateral is Polygon with 4 sides")
        super().display_info()
    
t1 = Triangle([5,9,10])
perimeter = t1.get_perimeter()
print("The Perimeter is:", perimeter)
t1.display_info()

q1 = Quadrilateral([4,5,4,5])
perimeter1 = q1.get_perimeter()
print("The Perimeter is:", perimeter)

q1.display_info()

        