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

class Deck:
    def __init__(self):
        self.cards = [Card(value) for value in range(1, 11)] * 4

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num_cards=1):
        for _ in range(num_cards):
            self.hand.append(deck.draw_card())

    def show_hand(self, hide_first_card=False):
        print(f"{self.name}'s hand:", end=' ')
        if hide_first_card:
            print("Hidden, ", end='')
            for card in self.hand[1:]:
                print(card, end=', ')
        else:
            for card in self.hand:
                print(card, end=', ')
        print(f"Total value: {self.hand_value()}")

    def hand_value(self):
        total = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.value == 1)
        while total <= 11 and aces:
            total += 10
            aces -= 1
        return total

class Blackjack:
    def __init__(self, player_name, money=100):
        self.player = Player(player_name)
        self.dealer = Player("Dealer")
        self.deck = Deck()
        self.money = money

    def deal_initial_cards(self):
        self.deck.shuffle()
        self.player.hand = []
        self.dealer.hand = []
        self.player.draw(self.deck, 2)
        self.dealer.draw(self.deck, 2)

        # Check if player gets blackjack
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
            return  # Player automatically wins with blackjack

        while True:
            self.player.show_hand()
            choice = input("Hit or stand? (h/s): ").lower()
            if choice == 'h':
                self.player.draw(self.deck)
                if self.player.hand_value() > 21:
                    print("Busted! You lose.")
                    return -1
            elif choice == 's':
                break

    def dealer_turn(self):
        while self.dealer.hand_value() < 17:
            self.dealer.draw(self.deck)

    def determine_winner(self):
        player_score = self.player.hand_value()
        dealer_score = self.dealer.hand_value()

        if player_score > 21:
            print("You busted! Dealer wins.")
            return -1
        elif dealer_score > 21:
            print("Dealer busted! You win.")
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
            bet = int(input("Place your bet: "))
            if bet > self.money:
                print("You don't have enough money.")
                continue

            if self.deal_initial_cards():
                continue

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

            if result == 1:
                print("\nYou won this round!")
                self.money += bet
            elif result == -1:
                print("\nYou lost this round!") 
                self.money -= bet

            if self.money <= 0:
                print("You're out of money! Game over.")
                break

            print(f"\nYour money: {self.money}")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

player_name = input("What's your name? ")
game = Blackjack(player_name)
game.play()
