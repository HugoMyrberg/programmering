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

        # ändra så att man inte ser dealerns första kort
        print("\nDealer's hand:")
        self.dealer.show_hand(hide_first_card=True)
        print("\nYour hand:")
        self.player.show_hand()

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
