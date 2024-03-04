Loggbok 
=========================
   
24 2 08

verqveqvb
---

Idag började jag att kolla på mitt egenprojekt.

Jag har valt att göra spelet Black Jack som mitt egenprojekt. Mina mål kommer att vara dessa.
Steg 1 är att skapa en Kortlek med fyra 1:or, fyra 2:or, osv... uptill fyra 13. 
Steg 2 blir att lägga till funktionen, blanda kortleken.
Steg 3 är att lägga till funktionen, dra ett kort ur leken.
Steg 4 blir, ge spelaren 2 kort.
Steg 5 är, ge datorn 1 kort.
steg 6 är att lägga till så att spelaren kan välja hit eller stand.
steg 7 Datorn väljer hit eller stand
steg 8 Vem vinner. Enkel summa. Korten värda 1 - 13.
steg 9 lägga till funktionen så att man kan lägga in och spela om pengar.
steg 10 Kunna spela en gång till.
steg 11 ange värde på korten, Knekt, dam, kung värda 10.
steg 12 Ess är värt 1 eller 11 beroende på.
steg 13 lägga till så man kan splitta sin handen om man får två lika. 
steg 14 lägga till eventuella fler regler.

Det kan tillkomma fler mål under tiden eller så kommer något att ändras. 

Än så länge har det gått bra och detta verkar roligt. 


24 1 22
---

Jag klarade test 10 förra lektinen så idag har jag börjat med mitt egenprojekt. Jag läste igenom uppgiften för att få en överblick om vad det är jag skall göra. 



24 1 15
---

Idag har jag fortsatt öva på test 10. Det går såder då jag tycker det är svårt och det finns inte så mycket varierande träningsundelag vilket gör att det blir svårt att förstå hur man skall göra. 

Exempel:
def maximum(a, b):
    # Funktionen maximum tar två argument a och b och returnerar det största av dem.
    return max(a, b)

def addera(x, y):
    # Funktionen addera tar två argument x och y och returnerar deras summa.
    return x + y

def hej(namn):
    # Funktionen hej tar ett argument namn och skriver ut en hälsning med det givna namnet.
    print("hej", namn)

23 12 4
---

Jag har övat på test 10. Det går bra men jag tycker det är lite svårt med allt men det går bra.


23 11 27
---
Jag övade på test 7 som jag hade omprov på och test 9.
Det gick bra och va ganska lätt.



23 11 20
---

# 7100-listor

Nu går det bra jag har fattat hur allt funkar.

 Exempel:
 import random 
tärningar = []
for i in range(20):
    kast = random.randint(1, 6)
    tärningar.append(kast)


23 11 13
---

### 7100-listor

Det går bättre och bättre, jag har börjat förstå hur det funkar.


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


