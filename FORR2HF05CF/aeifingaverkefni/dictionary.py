import random

dictionary = {"A":"Api","B":"Bannani","C":"Can","D":"Diskur","E":"Epli","F":"Fiskur","G":"Gull","H":"Hattur","I":"Inna","J":"Jól","K":"Kuldi","L":"Lækur","M":"Maður","N":"Nonni","O":"orgel",}

for x in dictionary:
    print(x,"er fyrir",dictionary[x])

print(dictionary["E"])
dictionary["H"] = "Halló"

dictionary.pop("C")
print(dictionary)

dictionary.popitem
# pop item tekur seiansta stakið sem var sett inn
print(dictionary)
dictafrit = dictionary

del dictionary
# ef maður reynir að prenta kemur "name 'dictionary' is not defined"
nyttdyct = {}
for x in range(1,6):
    nyttdyct[str(x)] = [str(random.randint(1,20))]
print(nyttdyct)

dictonary = {'1': ['16'], '2': ['4'], '3': ['10'], '4': ['11'], '5': ['15']}

for x, y in dictonary.items():
    print(x,y)

for x in dictonary.keys():
    print(x,"er lykill")

for x in dictonary.values():
    print(x,"er stak")

dictonary.clear()
# hreinsar dictionary
print(dictonary)