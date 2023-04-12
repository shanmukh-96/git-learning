domestic_animals = {"Dog", "Cat", "Elephant","Dog"}
wild_animals = {"Tiger", "Lion", "Elephant"}

print(domestic_animals)
print(wild_animals)

domestic_animals.add("Dolphin")
print(domestic_animals)

animals = domestic_animals | wild_animals
print(animals)

comman_animals = domestic_animals & wild_animals
print(comman_animals)