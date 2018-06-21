import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck(Card):

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for i in self.deck:
            deck_comp += i.__str__()+'\n'
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_crd = self.deck.pop()
        return deal_crd ## its a card class not the string, if we want to print the string do "return deal_crd.__str__(), this str method on Card call will do the priniting stuff

class Hand(Deck):
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        #print(card.rank)
        if card.suit == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:#this is equal to while self.value > 21 and self.aces>0:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self,total=200):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chip):
    while True:
        try:
            chip.bet = int(input('How much you wanna bet?'))
        except ValueError:
            print('Please enter valid integer chip count!')
        else:
            if chip.bet > chip.total:
                print('oops you dont have enough chips!!!')
            else:
                break

def hit(deck,hand):
    player_card = deck.deal()
    hand.add_card(player_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    playing = True

    while True:
        pl_choice = input('Hit or Stand? enter h or s')
        if pl_choice == 'h':
            hit(deck,hand)
        elif pl_choice == 's':
            print('player stands, Dealers hand')
            playing = False
        else:
            print('please enter only h or s')
            continue

        break

def show_some(player,dealer):

    print('Dealers card:\n')
    print('Note!! one card will be hidden for Dealer\n')
    print(dealer.cards[1])
    print('\n')
    print('player cards')
    for i in player.cards:
        print(i)

def show_all(player,dealer):

    print('Dealer cards:\n')
    for i in dealer.cards:
        print(i)
    print('\n')
    print('player_cards:\n')
    for i in player.cards:
        print(i)

def player_busts(player,dealer,chips):
    print('player busts, Dealer Wins')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('player wins!!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('player wins.. dealer busted!!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins.!!')
    chips.lose_bet()

def push(player,dealer):
    print('its a TIE!!')

while True:
    # Print an opening statement
    print('Welcome to BlackJack by Arun!')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    # Set up the Player's chips
    player_chips = Chips()


    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <=21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total
    print(f'player has {player_chips.total}')
    # Ask to play again
    wanna_play = input('wanna try again? y or n?')
    if wanna_play == 'y':
        playing = True
        continue
    else:
        playing = False
        print('Thank you!!')
        break
