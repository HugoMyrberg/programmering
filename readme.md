Loggbok 
===

24 04 22
---
Idag har jag gjort lite småändringar i min kod som har strulat tidigare. Det första jag gjorde var att ändra så att dealerns totala värde inte skulle synas. För att fixa detta la jag in följande:

        print(f"\nTotal value: {'Hidden' if hide_first_card else self.hand_value()}")

Det andra jag fixade var att fixa så att spelarens han inte kommer upp två gånger i rad. För att fixa detta tog jag bort följande i koden nedan:
 print("\nYour hand:")
        self.player.show_hand()

  # ändra så att man inte ser dealerns första kort
        print("\nDealer's hand:")
        self.dealer.show_hand(hide_first_card=True)
        print("\nYour hand:")
        self.player.show_hand()

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



24 4 4
---

Dagens lektion har jag fortsatt med mitt black jack projekt. Det går sakta men framåt. Det jag har fixat idag är att kolla igenom så att allt fungerar som det skall och det gör det. Jag har även frågat Rikard vad han tycker att jag skall lägga till eller ändra på. 


24 3 28
---

Idag har jag lagt in så man skall kunna spela mer en än gång och lagt till så datorn väljer vem som vinner. Det har gått bra och flytit på.

     def dealer_turn(self):
        while self.dealer.hand_value() < 17:
            self.dealer.draw(self.deck)

    def determine_winner(self):
        player_score = self.player.hand_value()
        dealer_score = self.dealer.hand_value()

        if player_score > 21:
            print("You went over 21! Dealer wins.")
            return -1
        elif dealer_score > 21:
            print("Dealer went over 21! You win.")
            return 1
        elif player_score > dealer_score:
            print("You win!")
            return 1
        elif player_score < dealer_score:
            print("Dealer wins.")
            return -1
        else:
            print("It's a tie.")
            return 0

24 3 21
---

Idag kändes det väldigt bra och allting flöt på och gick väldigt fort och bra. Det va lite krångligt på några ställen men efter lite snabb googling hitade jag någon lösning och impleterade eller ändrade det i min kod.

     def play(self):
        while True:
            print("\nNew round!")
            print(f"Your money: {self.money}")
            answer = input("Place your bet: ")
            if answer.isnumeric():  #ändra så det ändast tillåts med siffror och lägg till så att koden inte krashar om man skulle råka skriva något annat
                bet = int(answer)
                if bet <= self.money:
                    break
                else:
                    print("You don't have enough money.")
            else:
                print("Incorrect input. Please provide a numerical bet.")
                #ändra även här så ifall man skriver in fel kommando så skall koden inte krasha

        if self.deal_initial_cards():
            return

        self.player_turn()
        if self.player.hand_value() <= 21:
            self.dealer_turn()
            result = self.determine_winner()
        else:
            result = -1

24 3 14
--- 

Idag har jag fixat så att man kan spela flera omgångar så länge spelaren har pengar kvar, jag har även fixat lite smågrejer i hur datorn skall räkna ut vem som vinner och att ifall man säger nej till att spela igen så skall spelet avslutas. 

        print("\nDealer's hand:")
        self.dealer.show_hand()
        print("\nYour hand:")
        self.player.show_hand()
        # visa både spelarens och dealerns hand


         #om spelarens resultat är mer en dealerns alltså > 1 så skall spelaren vinna annars vinner dealern
        if result == 1:
            print("\nYou won this round!")
            self.money += bet
        elif result == -1:
            print("\nYou lost this round!") 
            self.money -= bet
      #pengar = eller < 0 så skall omgången avslutas och spelar får starta om
        if self.money <= 0:
            print("You're out of money! Game over.")
            return

        print(f"\nYour money: {self.money}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'n':  #ändra så att ifall man skriver allt annat en nej (n) så spelar man igen 
            print("Let's go again")
# fixa så att man kan spela fler än en gång
player_name = input("What's your name? ")
game = Blackjack(player_name)
for i in range(100):#räcker det med 100?
    game.play()
 

24 3 7
---

Dagens lektion ägnade jag åt att fortsätta med mitt black jack projekt. Idag la jag in så spelaren och datorn kan välja hit/h eller stand/s och att man kan välja hur mycket pengar man vill spela om. Dagens lektion har gått bra med det är svårt och tar tid. 

class Blackjack:
    def __init__(self, player_name, money=100):
        self.player = Player(player_name)
        self.dealer = Player("Dealer")
        self.deck = Deck()
        self.money = money
        #fixa så man kan välja hur mycket pengar man vill spela om 

    def deal_initial_cards(self):
        self.deck.shuffle()
        self.player.hand = []
        self.dealer.hand = []
        self.player.draw(self.deck, 2)
        self.dealer.draw(self.deck, 2)

24 2 29
---
 Idag har jag lagt till så att datorn skall räkna ut vem som vinner. Det gått bra jag känner mig mer och mer bekväm med att arbeta och der blir enklare och enklare att felsöka och hitta vad jag skall ändra. 

        # Kontrollera om spelaren får blackjack
        if self.check_blackjack() == 1:
            self.money += bet
            return True
        elif self.check_blackjack() == -1:
            self.money -= bet
            return True
        return False

    def check_blackjack(self):
        if len(self.player.hand) == 2 and self.player.hand_value() == 21:
            print("Blackjack! You win!")
            return 1
        elif len(self.dealer.hand) == 2 and self.dealer.hand_value() == 21:
            print("Dealer has Blackjack! You lose.")
            return -1
        return 0

    def player_turn(self):
        if self.check_blackjack() == 1:
            return  # Spelaren vinner automatiskt med blackjack
        while True:
            self.player.show_hand()
            choice = input("Hit or Stand? (h/s): ").lower()
            if choice == 'h':
                self.player.draw(self.deck)
                if self.player.hand_value() > 21:
                    print("Over 21! You lose.")
                    return -1
            elif choice == 's':
                break
            else:
                print("Unknown input, please try again")
                # ändra här så att ifall man skriver fel tecken så skall proggramet inte krasha

 

24 2 22
---

Idag fortsatte jag men mitt projekt. Idag stog det på listan att lägga till så att datorn delar ut korten till spelaren + datorn och lägga till lite smågrejer. Det går framåt men det är svårt och tar lång tid. Jag började att lägga till olika klaser för att göra det enklare och få en struktur i min kod. Efter det la jag in olika defenitioner som gör olika saker såsom visar upp spelarens hand, frågar efter spelarens namn med mera. 

 def draw_card(self):
        return self.cards.pop()
        #vad skall hände med kortleken

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num_cards=1):
        for _ in range(num_cards):
            self.hand.append(deck.draw_card())
        #visa spelaren hand

    def show_hand(self, hide_first_card=False):
        print(f"{self.name}'s hand:", end=' ')
        if hide_first_card:
            print("Hidden, ", end='')
            for card in self.hand[1:]:
                print(card, end=', ')
        else:
            for card in self.hand:
                print(card, end=', ')
        print(f"\nTotal value: {'Hidden' if hide_first_card else self.hand_value()}")

    def hand_value(self):
        total = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.value == 1)
        while total <= 11 and aces:
            total += 10
            aces -= 1
        return total
        #vad skall hända med spelaren


24 2 15
---

Under dagens lektion började jag med mitt projekt, jag började boka av min lista. Det var ganska svårt men efte mycket testande funkade det. Jag har lärt mig mycket om hur man tar sig vidare när man kör fast och att inte ge upp. Jag började att lägga in en import random där jag la in en kortlek med alla korts värden som blandas inan varje omgång. För att göra det enkelt skapar jag olika klasser som indikerar olika delar i spelat som till exempel, class card, class deck, class player osv...osv..

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


