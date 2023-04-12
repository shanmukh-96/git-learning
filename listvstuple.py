mixed_list = ["Helo", -7, 3.7,True]


print("1.", mixed_list[-1])
mixed_list[1]="Hi"

print("2.", mixed_list)

mixed_tuple = (3.5,"C++",7,False)

print("3.", mixed_tuple)
#mixed_tuple[2]="Hi"
print("3.", mixed_tuple)

mixed_list.append("Java")
mixed_list.insert(-2,"Java")
mixed_list.remove("Java")

print(mixed_list)
mixed_list.remove("Java")
print(mixed_list)