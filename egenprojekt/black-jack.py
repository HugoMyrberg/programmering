import random

class Kort:
    def __init__(self, värde):
        self.värde = värde

    def __str__(self):
        if self.värde == 1:
            return 'Ess'
        elif self.värde == 10:
            return 'Knekt'
        elif self.värde == 10:
            return 'Dam'
        elif self.värde == 10:
            return 'Kung'
        else:
            return str(self.värde)
            #kortens värde

class Kortlek:
    def __init__(self):
        self.kort = [Kort(värde) for värde in range(1, 11)] * 4

    def blanda(self):
        random.shuffle(self.kort)

    def dra_kort(self):
        return self.kort.pop()
        #vad skall hände med kortleken

class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.hand = []

    def dra(self, kortlek, antal_kort=1):
        for _ in range(antal_kort):
            self.hand.append(kortlek.dra_kort())
        #visa spelaren hand
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
        #vad skall hända med spelaren



class Blackjack:
    def __init__(self, spelare_namn, pengar=100):
        self.spelare = Spelare(spelare_namn)
        self.dealer = Spelare("Dealer")
        self.kortlek = Kortlek()
        self.pengar = pengar
        #fixa så man kan välja hur mycket pengar man vill spela om 

    def dela_ut_inledande_kort(self):
        self.kortlek.blanda()
        self.spelare.hand = []
        self.dealer.hand = []
        self.spelare.dra(self.kortlek, 2)
        self.dealer.dra(self.kortlek, 2)

        # ändra så att man inte ser dealerns första kort
        print("\nDealerns hand:")
        self.dealer.visa_hand(dölj_första_kort=True)
        print("\nDin hand:")
        self.spelare.visa_hand()

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
            else:
                print("Okänt tecken, försök igen")
                # ändra här så att ifall man skriver fel tecken så skall proggramet inte krasha

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
            if svar.isnumeric():  #ändra så det ändast tillåts med siffror och lägg till så att koden inte krashar om man skulle råka skriva något annat
                insats = int(svar)
                if insats <= self.pengar:
                    break
                else:
                    print("Du har inte tillräckligt med pengar.")
            else:
                print("Felaktig inmatning. Var god ange en numerisk insats.")
                #ändra även här så ifall man skriver in fel kommando så skall koden inte krasha

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
        # visa både spelarens och dealerns hand


         #om spelarens resultat är mer en dealerns alltså > 1 så skall spelaren vinna annars vinner dealern
        if resultat == 1:
            print("\nDu vann denna omgång!")
            self.pengar += insats
        elif resultat == -1:
            print("\nDu förlorade denna omgång!") 
            self.pengar -= insats
      #pengar = eller < 0 så skall omgången avslutas och spelar får starta om
        if self.pengar <= 0:
            print("Du är utan pengar! Spelet är över.")
            return

        print(f"\nDina pengar: {self.pengar}")
        spela_igen = input("Vill du spela igen? (j/n): ").lower()
        if spela_igen == 'n':  #ändra så att ifall man skriver allt annat en nej (n) så spelar man igen 
            return
        else:
            print("Vi kör igen")
# fixa så att man kan spela fler än en gång
spelare_namn = input("Vad är ditt namn? ")
spel = Blackjack(spelare_namn)
for i in range(100): #räcker det med 100?
    spel.spela()

    

