Loggbok 
=========================

24 04 15
---

Idag ändrade jag så att man kan se dealerns första kort. 
# Visa endast dealerns första kort
        print("\nDealerns hand:")
        self.dealer.visa_hand(dölj_första_kort=True) 
        print("\nDin hand:")
        self.spelare.visa_hand()

24 04 11
---

Förra lektionen fick jag lite grejer av Rikard som han tycker att jag skulle ändra eller lägga till i min kod och det var bland annat ändra så att min kod inte krashar om man skulle råka skriva in en siffra eller något konstigt tecken istället för ord. Jag har även fixat så man kan spela flera gånger i rad. 

Det jag fick lägga in såg ungefär ut såhär beroende på var i koden det skulle fixas.
            else:
                print("Felaktig inmatning. Var god ange en numerisk insats.")

Det gick helt okej idag men jag fick diskuttera och bolla lite ideer med Rikard för att koden skulle bli så enkel och lätt som möjligt. 



24 3 21
---

Dagens lektion har jag fortsatt med mitt black jack projekt. Det går sakta men framåt. Det jag har fixat idag är att kolla igenom så att allt fungerar som det skall och det gör det. Jag har även frågat Rikard vad han tycker att jag skall lägga till eller ändra på. 


24 3 14
---

Idag har jag lagt in så man skall kunna spela mer en än gång och lagt till så datorn väljer vem som vinner. Det sista jag gjorde var även att lägga till så man kan splita handen om man får två lika dana. 

    def dealerns_runda(self):
        while self.dealer.hand_värde() < 17:
            self.dealer.dra(self.kortlek)

    def avgör_vinnaren(self):
        spelarens_poäng = self.spelare.hand_värde()
        dealerns_poäng = self.dealer.hand_värde()

        if spelarens_poäng > 21:
            print("Du gick över 21! Dealern vinner.")
            return -1
        elif dealerns_poäng > 21:
            print("Dealern gick över 21! Du vinner.")
            return 1
        elif spelarens_poäng > dealerns_poäng:
            print("Du vinner!")
            return 1
        elif spelarens_poäng < dealerns_poäng:
            print("Dealern vinner.")
            return -1
        else:
            print("Det är oavgjort.")
            return 0

    def spela(self):
        while True:
            print("\nNy omgång!")
            print(f"Dina pengar: {self.pengar}")
            svar = input("Placera din insats: ")
            if svar.isnumeric():
                insats = int(svar)
                if insats <= self.pengar:
                    break
                else:
                    print("Du har inte tillräckligt med pengar.")

        if self.dela_ut_inledande_kort():
            return

        self.spelarens_runda()
        if self.spelare.hand_värde() <= 21:
            self.dealerns_runda()
            resultat = self.avgör_vinnaren()
        else:
            resultat = -1

        print("\nDealerns hand:")
        self.dealer.visa_hand()
        print("\nDin hand:")
        self.spelare.visa_hand()

        if resultat == 1:
            print("\nDu vann denna omgång!")
            self.pengar += insats
        elif resultat == -1:
            print("\nDu förlorade denna omgång!") 
            self.pengar -= insats

        if self.pengar <= 0:
            print("Du är utan pengar! Spelet är över.")
            return

        print(f"\nDina pengar: {self.pengar}")
        spela_igen = input("Vill du spela igen? (j/n): ").lower()
        if spela_igen == 'n':
            return
        else:
            print("Vi kör igen")

spelare_namn = input("Vad är ditt namn? ")
spel = Blackjack(spelare_namn)
for i in range(100):
    spel.spela()

Idag kändes det väldigt bra och allting flöt på och gick väldigt fort och bra. Det va lite krångligt på några ställen men efter lite snabb googling hitade jag någon lösning och impleterade eller ändrade det i min kod. 

24 3 7
---

Dagens lektion ägnade jag åt att fortsätta med mitt black jack projekt. Idag la jag in så spelaren och datorn kan välja hit/h eller stand/s, att man kan välja hur mycket pengar man vill spela om och att datorn skall räkna ut vem som vinner. Idag har det gått bra jag känner mig mer och mer bekväm med att arbeta och der blir enklare och enklare att felsöka och hitta vad jag skall ändra. 

class Blackjack:
    def __init__(self, spelare_namn, pengar=100):
        self.spelare = Spelare(spelare_namn)
        self.dealer = Spelare("Dealer")
        self.kortlek = Kortlek()
        self.pengar = pengar

    def dela_ut_inledande_kort(self):
        self.kortlek.blanda()
        self.spelare.hand = []
        self.dealer.hand = []
        self.spelare.dra(self.kortlek, 2)
        self.dealer.dra(self.kortlek, 2)

        # Kontrollera om spelaren får blackjack
        if self.kontrollera_blackjack() == 1:
            self.pengar += insats
            return True
        elif self.kontrollera_blackjack() == -1:
            self.pengar -= insats
            return True
        return False

    def kontrollera_blackjack(self):
        if len(self.spelare.hand) == 2 and self.spelare.hand_värde() == 21:
            print("Blackjack! Du vinner!")
            return 1
        elif len(self.dealer.hand) == 2 and self.dealer.hand_värde() == 21:
            print("Dealern har Blackjack! Du förlorar.")
            return -1
        return 0

    def spelarens_runda(self):
        if self.kontrollera_blackjack() == 1:
            return  # Spelaren vinner automatiskt med blackjack

        while True:
            self.spelare.visa_hand()
            val = input("Ta eller stanna? (t/s): ").lower()
            if val == 't':
                self.spelare.dra(self.kortlek)
                if self.spelare.hand_värde() > 21:
                    print("Över 21! Du förlorar.")
                    return -1
            elif val == 's':
                break

Idag fick jag mycket gjort vilket känns väldigt bra. Det var ganska svårt och jobbigt men med hjälp av rikard och lite googling hitade jag lösningar som jag kunde lägga in i min kod för att få allt att fungera.  

24 2 22
---

Idag fortsatte jag men mitt proejkt. Idag stog det på listan att lägga till så att datorn delar ut korten till spelaren + datorn. Det går framåt men det är svårt och tar lång tid. 

 def dra_kort(self):
        return self.kort.pop()

class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.hand = []

    def dra(self, kortlek, antal_kort=1):
        for _ in range(antal_kort):
            self.hand.append(kortlek.dra_kort())

    def visa_hand(self, dölj_första_kort=False):
        print(f"{self.namn}s hand:", end=' ')
        if dölj_första_kort:
            print("Dolt, ", end='')
            for kort in self.hand[1:]:
                print(kort, end=', ')
        else:
            for kort in self.hand:
                print(kort, end=', ')
        print(f"Totalt värde: {self.hand_värde()}")

    def hand_värde(self):
        totalt = sum(kort.värde for kort in self.hand)
        ess = sum(1 for kort in self.hand if kort.värde == 1)
        while totalt <= 11 and ess:
            totalt += 10
            ess -= 1
        return totalt


24 2 15
---

Under dagens lektion började jag med mitt projekt, jag började boka av min lista. Det var ganska svårt men efte mycket testande funkade det. Jag har lärt mig mycket om hur man tar sig vidare när man kör fast och att inte ge upp. Jag började att lägga in en import random där jag la in en kortlek med alla korts värden som blandas inan varje omgång.

import random

class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 1:
            return 'Ace'
        elif self.value == 10:
            return 'Jack'
        elif self.value == 10:
            return 'Queen'
        elif self.value == 10:
            return 'King'
        else:
            return str(self.value)
            #kortens värde

class Deck:
    def __init__(self):
        self.cards = [Card(value) for value in range(1, 11)] * 4

    def shuffle(self):
        random.shuffle(self.cards)

   
24 2 08
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
steg 8 Vem vinner. Enkel summa. Korten värda 1 - 10.
steg 9 lägga till funktionen så att man kan lägga in och spela om pengar.
steg 10 Kunna spela en gång till.
steg 11 ange värde på korten, Knekt, dam, kung värda 10.
steg 12 Ess är värt 1 eller 11 beroende på.
steg 13 lägga till så man kan splitta sin handen om man får två lika. 
steg 14 lägga till eventuella fler regler.
steg 15 lägg till så man kan spela flera gånger i rad
steg 16 lägg till så att koden inte krashar om man skriver fel

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


