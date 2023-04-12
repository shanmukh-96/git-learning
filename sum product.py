number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

def add_numbers(n1, n2):
    result = n1 + n2
    return result

def multiply_numbers(n1, n2):
    result = n1 * n2
    return result

sum = add_numbers(number1, number2)
product = multiply_numbers(number1, number2)

print("The sum of the numbers is :", sum)
print("The product of the number is :", product)
