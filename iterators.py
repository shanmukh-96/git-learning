numbers = [2,5,6]

value = numbers.__iter__()

# print(value)

item1 = value.__next__()

item2 = value.__next__()
item3 = next(value)

print(item1)
print(item2)
print(item3)