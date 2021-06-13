import random, os, time
os.system("cls")
running = True

class Cards():
    def __init__(self):
        self.cards = []
        self.deck = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]*4
        self.dealer_cards = []
        self.allow_hit = True
        self.bet = 0
        self.doubled = False

        random.shuffle(self.deck) # Shuffle the deck
        self.dealer_cards.append(self.deck.pop()) # Give a card to the dealer
        random.shuffle(self.deck) # Shuffle the deck again
        self.dealer_cards.append(self.deck.pop()) # Give a card to the dealer again
    
    def total(self, deck):
        self.card_sum = 0
        for card in deck:
            if card == "A":
                if self.card_sum + 11 <= 21:
                    self.card_sum += 11
                else:
                    self.card_sum += 1
            else:
                if type(card) == str: self.card_sum += 10
                else: self.card_sum += card
        
        return self.card_sum

    def generate(self):
        global running
        while True:
            try: self.bet = int(input(f"{colorObj.PURPLE}How much would you like to bet? {colorObj.RESET}$"))
            except ValueError: print(f"{colorObj.YELLOW}Incorrect value, try again{colorObj.RESET}")
            else: break

        random.shuffle(self.deck) # Shuffle the deck
        self.cards.append(self.deck.pop()) # Give a card to the player
        random.shuffle(self.deck) # Shuffle deck
        self.cards.append(self.deck.pop()) # Give a card to the player again
        print(f"Your cards:", self.total(self.cards), self.cards, "\n")
        if self.total(self.cards) == 21:
            print(f"{colorObj.GREEN}Blackjack! You win!{colorObj.RESET}")
            running = False


    def hit(self):
            random.shuffle(self.deck) # Shuffle the deck
            new_card = self.deck.pop() # Get a new card for the player
            print(f"You got: {new_card}")
            self.cards.append(new_card)
            print("Your cards:", self.total(self.cards), self.cards, "\n")
            del new_card

    def score(self):
        global running
        if self.allow_hit:
            print(f"Dealer cards:", self.total([self.dealer_cards[0], 10]), [self.dealer_cards[0], "?"])
        else:
            print(f"Dealer cards:", self.total(self.dealer_cards), self.dealer_cards)
        print(f"Your cards:", self.total(self.cards), self.cards, "\n")
        
        if self.total(self.cards) == 21:
            print(f"{colorObj.GREEN}Blackjack! You win!{colorObj.RESET}")
            running = False

        elif self.total(self.dealer_cards) == 21 and not self.allow_hit:
            print(f"{colorObj.RED}Dealer got a Blackjack, you lose!{colorObj.RESET}")
            running = False

        elif self.total(self.cards) > 21:
            print(f"{colorObj.RED}You busted! You lose!{colorObj.RESET}")
            running = False

    def stand(self):
        global running
    
        def dealer_sum_check():
            if self.total(self.dealer_cards[:2]) > 17:
                time.sleep(1)
                print(f"Dealer cards:", self.total(self.dealer_cards), self.dealer_cards)

        while not (self.total(self.dealer_cards) >= 17): # While the dealers sum is lower than 17:
            random.shuffle(self.deck) # Shuffle the deck
            self.dealer_cards.append(self.deck.pop()) # Give a card to the dealer
            print(f"Dealer cards:", self.total(self.dealer_cards), self.dealer_cards) # Display the cards
            time.sleep(1) # Wait a second

            if self.total(self.dealer_cards) > 21: # If the dealers sum is larger than 21
                print(f"{colorObj.GREEN}Dealer busted! You win!{colorObj.RESET}")
                running = False

            elif self.total(self.dealer_cards) == 21: # If the dealer gets a sum of 21
                print(f"{colorObj.RED}Dealer got a Blackjack, you lose!{colorObj.RESET}")
                running = False

        if self.total(self.dealer_cards) == self.total(self.cards): # If sum of dealer cards are same as sum of player cards
            dealer_sum_check()
            print(f"{colorObj.RED}You both got the same sum. Push!{colorObj.RESET}")
            running = False
        
        if self.total(self.cards) < self.total(self.dealer_cards) and self.total(self.dealer_cards) < 21: # If player sum is lower than the dealers
            dealer_sum_check()
            print(f"{colorObj.RED}Your score is lower than the dealers. You lose!{colorObj.RESET}")
            running = False
        
        elif self.total(self.cards) > self.total(self.dealer_cards) and self.total(self.cards) < 21: # If player sum is higher than the dealers
            dealer_sum_check()
            print(f"{colorObj.GREEN}Your score is higher than the dealers. You win!{colorObj.RESET}")
            running = False

        print("Your cards:", self.total(self.cards), self.cards, "\n")
    
    def double(self): #FIXME
        self.bet *= 2
        print(f"{colorObj.CYAN}You have doubled your bet to {colorObj.BOLD}{self.bet}${colorObj.RESET}{colorObj.CYAN}!{colorObj.RESET}")
        time.sleep(1)
        self.hit()
        playerObj.score()
        if running:
            time.sleep(1)
            self.stand()

class Color():
    def __init__(self):
        self.PURPLE = "\033[95m"
        self.CYAN = "\033[96m"
        self.DARKCYAN = "\033[36m"
        self.BLUE = "\033[94m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.RED = "\033[91m"
        self.BOLD = "\033[1m"
        self.UNDERLINE = "\033[4m"
        self.RESET = "\033[0m"

colorObj = Color()

playerObj = Cards()

playerObj.generate()
print("Dealer cards:", playerObj.total([playerObj.dealer_cards[0], 10]), [playerObj.dealer_cards[0], "?"], "\n")

while running:
    choice = input(f"""{colorObj.CYAN}[{colorObj.BOLD}H{colorObj.RESET}{colorObj.CYAN}]it, 
[{colorObj.BOLD}S{colorObj.RESET}{colorObj.CYAN}]tand {colorObj.RESET}{colorObj.CYAN}or
[{colorObj.BOLD}D{colorObj.RESET}{colorObj.CYAN}]ouble? {colorObj.RESET}""").lower()
    if choice in ["h", "hit", "s", "stand", "d", "double"]:
        if choice in ["h", "hit"]:
            if playerObj.allow_hit:
                playerObj.hit()
            else:
                print(f"{colorObj.RED}Not allowed{colorObj.RESET}")
        
        elif choice in ["s", "stand"]:
            playerObj.allow_hit = False
            playerObj.stand()
        
        elif choice in ["d", "double"]:
            playerObj.doubled = True
            playerObj.double()
            playerObj.allow_hit = False

        if not playerObj.doubled: playerObj.score()
    else:
        print(f"{colorObj.RED}Invalid choice{colorObj.RESET}")