Loggbok 
=========================



23 11 06
---

### 7100-listor

exempel:
x = [2, 3, 2, 4, 1]
x [1] = 5
x [-1] = 6
x.append (4)
print(x)
medel = sum(x) / len(x)
print(medel)
x.sort()
print("sorterad:", x)

Det gick inte så bra då jag tycker detta är väldigt svårt och jag fattar inte riktigt hur man gör

23 10 23
---

### 7100 listor

exempel:
#Det som visas efter hashtag (#) nedan är det som
#skrivs ut av print

inköpslista = ["bröd", "smör", "ost"]
print(inköpslista)
#['bröd', 'smör', 'ost']

det gick bra och va inte så svårt



23 10 16
---

### 7073 flödesdiagram

exempel:
text = input("Ange ett heltal: ")
tal = int(text)
if tal % 2 == 0:
    print('talet är jämnt')
else:
    print('talet är udda')
print('klart')

det gick bra och var inte svårt




23 10 9
---

gjorde:
### 7061 slingor-mer while

exempel:

svar = int(input("skriv ett tal"))
antal_gissningar = 1


while svar != 42 and antal_gissningar <3:
    if svar < 42:
        print("för litet")
        svar = int(input("gissa igen:  "))

    if svar > 42:
        print("för stort. ")
        svar = int(input("gissa igen: "))

    antal_gissningar = antal_gissningar + 1
if svar == 42:
    print("du är bäst")
print(antal_gissningar, "är tyvärr det maximala antal gissningar du får på dig. Vill du köra igen så starta om programmet")


det gick såder då jag inte riktigt fattade hur man skulle göra och koden krånglade.
Men jag fick hjälp av Rikard och förstod till slut vad koden gjorde och hur det fungerade.






23 10 2
---

gjorde:

### 7061 slingor-mer while

exempel:

svar = int(input("skriv ett tal"))
antal_gissningar = 1

while svar != 42:
    if svar < 42:
        print("för litet")
        svar = int(input("gissa igen:  "))

    if svar > 42:
        print("för stort. ")
        svar = int(input("gissa igen: "))
    antal_gissningar = antal_gissningar + 1
print(antal_gissningar, "gisningar behövde du")

det gick bra och va lite svårare en förra veckans while slingor
har lärt mig lite mer och det känns bra





23 09 18
---

gjorde:

### 7070 slumptal

exempel:
import random
i = 0
while i < 5:
    t1 = random.randrange(1,7)
    t2 = random.randrange(1,7) 
    print("tärning 1:", t1)
    print("tärning 2:", t2)
    summa = t1 + t2
    print("Summan av tärningskasten är:", summa)
    i = i + 1


det gick såder eftersom det var väldigt svårt och jag fattade inte riktigt 







23 09 11
---

gjorde:

### 7060 slingor-while

Exempel:

i = 10
while i < 11:
    print(i)
    i = i+2
print("klar")

Det gick bra
Va inte så svårt nu när man har kommit in i det och förstår hur python fungerar


23 09 4
----------------

Gjorde:
### 7050 if-sats

Exempel:

svar = int(input("skriv ett heltal"))
if svar > 42:
    print ("för stort")
elif svar < 42:
    print("för litet")
else:
    print("rätt")


Det gick bra men det va lite svårt eftersom allt är nytt för mig




23 08 28 
-------

Installerade Python 
det gick bra
inget va svårt

Gjorde: 

### 7040 in- och utmaning

Exempel:

a=20
b=25
print(a)
print(b)


