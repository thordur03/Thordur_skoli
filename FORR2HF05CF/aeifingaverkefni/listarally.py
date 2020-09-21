import random

listi = []

for x in range(101):
    listi.append(random.randint(34,68))
a = sum(listi)
while sum(listi)>4500:
    listi.pop(0)
print("sortaður listi",sorted(listi))
print("meðaltal listans",round(sum(listi)/len(listi),2))
print("Stærsta talan: ",max(listi))
print("Minsta talan: ", min(listi))

listi40 = []
listi2 = []
tal = 0
for x in listi:
    if x%5!=0:
        listi2.append(x)
    
listi = sorted(listi2.copy())
print("listinn án talna sem ganga upp í 5",listi)
tal = 0
for x in listi:
    if x == 41:
        listi.pop(tal)
        listi40.append(41)
print(listi40)




