heros = ['spider man','thor','hulk','iron man','captain america']

print("The length of the heros list: ", len(heros))

heros.append('black panther')
print(heros)

# print('\n', dir(heros))

heros.remove('black panther')
print(heros)

for i in range(len(heros)):
    if heros[i] == 'thor':
        heros[i+1] = 'black panther'
        
print(heros)


for i in range(len(heros)):
    if heros[i] == 'thor':
        heros.pop(i)
        heros.insert(i, 'doctor strange')

print(heros)
heros.sort()

print("heros list in alphabetical order: \n ", heros)