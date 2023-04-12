marks = [55,64,75,80,65]

def find_avg_marks(marks):
    sum_marks = sum(marks)
    length = len(marks)
    result = sum_marks/length
    return result

def find_grade(average):
    if average >= 80:
        print("Your grade is A")
    elif average < 80 and average >= 60:
        print("Your grade is B")
    elif average < 60 and average <= 50:
        print("Your grade is C")
    else:
        print("Your grade is F")
        
average = find_avg_marks(marks)
print("The average marks is:", average)
student_grade = find_grade(average)