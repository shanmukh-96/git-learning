class Student:
    
    def check_pass_fail(self):
        
        if self.marks >=40:
            return True
        else:
            return False
            
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
student1 = Student("Harry", 90)
student2 = Student("Larry", 20)

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)
        