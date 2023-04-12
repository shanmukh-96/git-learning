expense = [2200, 2350, 2600, 2130, 2190]

extra_expense = expense[1] - expense[0]

print("The extra expense spend in Feb compare to January: ", extra_expense)

def first_quater_expense():
    sum = 0
    for i in range(3):
        sum = sum + expense[i]
        print(i)
    return sum

print("The first Quater expenses are: ", first_quater_expense())

for i in range(len(expense)):
    if expense[i] == 2000:
        print("The index of expense having 2000: ", i)
    
expense.append(1980)
print(expense)

expense[3] = expense[3] - 200
print(expense)