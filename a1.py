#Jastejpal Soora
#Program to determine Poker hand

hand = input("Enter your hand: ")

while(len(hand) < 10 or len(hand) > 10): #Loops input of poker hand in case of typing errors
    print("You did not enter 5 cards")
    hand = input("Enter your hand: ")

def main():
    rank = '23456789TJQKA'
    suit = 'cdhs'
    upperRank = hand.upper() #To ensure that the uppercase of the rank is taken regardless of how it was inputted
    lowerSuit = hand.lower() #To ensure that the lowercase of the suit is taken regardless of how it was inputted

    def FourofaKind(hand): #Function that determines four of a kind
        for num in rank:
            if upperRank.count(num) == 4:
                return True

    def ThreeofaKind(hand): #Function that determines three of a kind
        for num in rank:
            if upperRank.count(num) == 3:
                return True

    def pair(hand): #Function that determines a pair
        for num in rank:
            if upperRank.count(num) == 2:
                return True

    def flush(hand): #Function that determines a flush
        if lowerSuit[1] == lowerSuit[3] == lowerSuit[5] == lowerSuit[7] == lowerSuit[9]:
            return True
          
    def high(hand): #Function that determines the highest rank in the hand
        i = 12     
        while i > 0:
            for char in hand:
                if rank[i] == char:
                    return char             
            i -= 1
        
    def evaluate(hand): #Function that determines the inputted poker hand
        if flush(hand) == True:
            print("flush")
        elif FourofaKind(hand) == True:
            print("four of a kind")
        elif ThreeofaKind(hand) == True and pair(hand) == True:
            print("full house")
        elif ThreeofaKind(hand) == True:
            print("three of a kind")
        elif pair(hand) == True:
            print("pair")
        else:
            print(high(hand), "high")
    evaluate(hand)

main()

