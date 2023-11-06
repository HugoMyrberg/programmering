'''
x = [2, 3, 2, 4, 1]
x [1] = 5
x [-1] = 6
x.append (4)
print(x)
medel = sum(x) / len(x)
print(medel)
x.sort()
print("sorterad:", x)
'''
'''
import random 
tärningar = []
for i in range(20):
    kast = random.randint(1, 6)
    tärningar.append(kast)

antal_3 = 0
for tärning in tärningar:
    if tärning == 3:
        antal_3 = antal_3+1
print(tärningar)
print(antal_3)



