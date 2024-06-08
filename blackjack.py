import random

class Card:
    def __init__(self, suit, value):
        valid_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        valid_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        if suit not in valid_suits:
            raise ValueError("Invalid suit")
        if value not in valid_values:
            raise ValueError("Invalid value")

        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No cards left in the deck.")
            return None

    def __str__(self):
        return f"Deck with {len(self.cards)} cards"

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        total_value = 0
        num_aces = 0
        for card in self.cards:
            if card.value in ["Jack", "Queen", "King"]:
                total_value += 10
            elif card.value == "Ace":
                total_value += 11
                num_aces += 1
            else:
                total_value += int(card.value)

        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value

    def bust(self):
        return self.calculate_value() > 21

    def __str__(self):
        return ", ".join(map(str, self.cards))

    def bust(self):
        return self.calculate_value() > 21

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, card):
        self.hand.add_card(card)

    def stand(self):
        pass  # Player chooses to stand, no action needed

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def deal_card(self, card):
        self.hand.add_card(card)

    def hit(self, card):
        self.hand.add_card(card)

    def stand(self):
        pass  # Dealer chooses to stand, no action needed

class Game:
    def __init__(self, player_name):
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer()
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0

    def play_round(self):
        # Reset hands
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.player.hand = Hand()
        self.dealer.hand = Hand()

        # Deal initial cards
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())

        # Show hands
        print("Player's Hand:", self.player.hand.cards[0], "and [Hidden Card]")
        print("Dealer's Hand:", self.dealer.hand.cards[0], "and [Hidden Card]")

        # Player's turn
        while not self.player.hand.bust():
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                self.player.hit(self.deck.deal_card())
                print("Player's Hand:", self.player.hand)
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

        # Dealer's turn
        while self.dealer.hand.calculate_value() < 17:
            self.dealer.hit(self.deck.deal_card())

        # Determine winner
        player_value = self.player.hand.calculate_value()
        dealer_value = self.dealer.hand.calculate_value()
        print("Player's Hand:", self.player.hand, "Value:", player_value)
        print("Dealer's Hand:", self.dealer.hand, "Value:", dealer_value)
        if player_value > 21:
            print("Player busts! Dealer wins.")
            self.dealer_wins += 1
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
            self.player_wins += 1
        elif player_value > dealer_value:
            print("Player wins!")
            self.player_wins += 1
        elif dealer_value > player_value:
            print("Dealer wins!")
            self.dealer_wins += 1
        else:
            print("It's a tie!")
            self.ties += 1

    def play_game(self):
        while True:
            self.play_round()
            print("Player Wins:", self.player_wins)
            print("Dealer Wins:", self.dealer_wins)
            print("Ties:", self.ties)
            again = input("Do you want to play another round? (y/n): ").lower()
            if again != 'y':
                break

# Example usage:
player_name = input("Enter your name: ")
game = Game(player_name)
game.play_game()
