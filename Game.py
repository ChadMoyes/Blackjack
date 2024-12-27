import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 

    def __str__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suit in self.suits:
            for value in range(1,14):
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        #This will add a card to the players hand
        self.hand.append(card)
    
    def calculate_hand(self):
        total_value = 0
        ace_count = 0 

        for card in self.hand:
            total_value += card.value
            if card.value == 1:
                ace_count += 1
        
        while total_value <= 11 and ace_count:
            total_value += 10
            ace_count -= 1

        return total_value 
    
    def show(self):
        return ", ".join(str(card) for card in self.hand)
    
class Dealer(Player):
    def __init__(self):
        super().__init__(Dealer)

    def show_hand(self, reveal_cards=False):
        if reveal_cards:
            return ', '.join(str(Card) for Card in self.hand)
        else:
            if self.hand:
                return f"{self.hand[0]}, [hidden]"
            return "[No cards]"
    
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Dealer()
    
    def deal_first_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

        if self.player.calculate_hand() == 21:
            print(f"Your hand is: {self.player.show()} (Total: {self.player.calculate_hand()})")
            print("Blackjack! You win the game.")
            return True
        return False

    def players_turn(self):
        while True:
            print(f"Your hand: {self.player.show()} (Total: {self.player.calculate_hand()})")
            print(f"Dealers hand: {self.dealer.show_hand()}")

            choice = input("Would you want to hit or stand? (hit/stand): ").strip().lower()

            if choice == "hit":
                self.player.add_card(self.deck.deal_card())
                if self.player.calculate_hand() > 21:
                    print(f"Your hand is: {self.player.show()} (Total: {self.player.calculate_hand()})")
                    print("Its a bust! Dealer wins the game.")
                    return False
            elif choice == "stand":
                return True
            else:
                print("Invalid answer. Please choose one of the following (hit/stand)")

    def dealers_turn(self):
        print(f"Dealers full hand: {self.dealer.show_hand(reveal_cards=True)}")
        while self.dealer.calculate_hand() < 17:
            self.dealer.add_card(self.deck.deal_card())
        
        print(f"Dealers updated full hand: {self.dealer.show_hand(reveal_cards=True)} (Total: {self.dealer.calculate_hand()})")
        if self.dealer.calculate_hand() > 21:
            print("The Dealer has busted! You win the game.")
            return False
        return True
    
    def winner(self):
        players_total = self.player.calculate_hand()
        dealers_total = self.dealer.calculate_hand()

        print(f"Your total is: {players_total}")
        print(f"Dealers total is: {dealers_total}")

        if players_total > dealers_total:
            print("You win the game!")
        elif dealers_total > players_total:
            print("The dealer has won.")
        else:
            print("It is a tie!")

    def play_game(self):
        print("Let us play Blackjack")
        self.deal_first_cards()

        print(f"Dealers hand: {self.dealer.show_hand()}")
        print(f"Players hand: {self.player.show()}")

        if not self.players_turn():
            return
        if not self.dealers_turn():
            return
        
        self.winner()

if __name__ == "__main__":
    game = BlackjackGame()
    game.play_game()