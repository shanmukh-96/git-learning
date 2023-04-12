try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    
    result = num / den
    print(result)
    
    list = [3,6,6,6]
    index = int(input("Enter index: "))
    print(list[index])
except ZeroDivisionError:
    print("The denominator cannot be Zero. please try again.")
    
except IndexError:
    print("The index cannot be  greater than the size of list. please try again")
    
print("End of program")