import random
from functions import *

def format_card(card) -> str:
    suit = {1: "A", 11: "J", 12: "Q", 13: "K"}
    if card in suit:
        return suit[card]
    return card
      
class Card:
    def __init__(self, card) -> None:
        self.face = format_card(card)
        self.num = card

class Deck:
    def __init__(self):
        self.reset()
    def reset(self):
        self.deck = []
        for num in range(12):
            self.deck.append(Card(num+2))
    def deal(self):
        print(">Delt cards are:")
        self.card1 = self.take(random.randint(2, len(self.deck)+1))
        self.card2 = self.take(random.randint(2, len(self.deck)+1))
        self.card3 = self.take(random.randint(2, len(self.deck)+1))
        if self.card2.num < self.card1.num: self.card1, self.card2 = self.card2, self.card1
        print(f" {self.card1.face}")
        print(f" {self.card2.face}")
    def take(self, card):
        delt_card = self.deck[card-2]
        if  not delt_card: return
        self.deck.pop(card-2)
        return delt_card

def ask(curr_money):
    while True:
        try:
            answer = int(input(" How much are you betting!"))
            if answer <= curr_money:
                return answer
            else:
                print(" You don't have that much, please bet less!")
        except ValueError:
            print(" Not a number!")
            pass

def main():
    clearConsole()
    money = 100
    print(f"Welcome to acey ducey!\nYou will be delt 2 random cards\nyou can bet your money\non wether the card will be between the 2 delt cards!\nYour starting amount is {money}$")
    rounds = 0
    while money > 0:
        rounds += 1
        deck = Deck()
        deck.deal()
        bet = ask(money)
        if bet == 0:
            print(" CHICKEN!!!")
            continue
        print(f" Your card was {deck.card3.face}!")
        if deck.card3.num > deck.card1.num and deck.card3.num < deck.card2.num:
            money += bet
            print(f" You got {bet}$, now you have {money}$")
            continue
        money -= bet
        print(f" You lost {bet}$, now you have {money}$")
    print(">You ran out of money!")
    print(f" You played for {rounds} rounds!")

if __name__ == "__main__":
    money = 100
    main()
