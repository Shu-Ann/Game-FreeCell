#!/usr/bin/env python
# coding: utf-8


class Card:
    # create a list for card face from 1~13 (its value)
    face = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # create a list for card suit ,Clubs=C, Diamonds=D, Spades=S, Hearts=H
    suit = ['C', 'D', 'S', 'H']
    
    #constructor
    #to set up the initial card
    def __init__(self, card_face=None, card_suit=None):
        
        self.card_face=card_face
        self.card_suit=card_suit
    
    #visulaize the suit and unify tens digit to one character
    #use icon to represent suits ex: Clubs=♣️
    #to represent face as str type and unify tens into a character
    #return card as set up for ex:(1,'C')=(A♣️)
    def __repr__(self):
        
        suitlist={'C':'♣️', 'D':'♦️','S':'♠️', 'H':'♥️'} 
        facedic={**{f:str(f) for f  in range(2,11)},**{1:'A',10:'T',11:'J', 12:'Q',13:'K'}} 
        return facedic[self.card_face]+suitlist[self.card_suit]
   
    #display function
    def display(self):
        return self.__repr__()
        
        
    #accessors
    #to access the card face
    def get_card_face(self):
        return self.card_face

    #to access the card suit
    def get_card_suit(self):
        return self.card_suit
    
    #mutators
    def set_card(self, setface, setsuit):
        
        self.card_suit=setsuit
        self.card_face=setface
        return Card(setsuit, setface)



# uncomment to test
#have two test ways
#one is let user input then test if users' input successed, the other is to set up a card already for testing Card()

# def main():
#     a=int(input("Please input the values of card face(1~13):"))
#     b=input("Please input the suit of card (Clubs=C, Diamonds=D, Spades=S, Hearts=H):")
#     while a not in Card.face or b not in Card.suit : #check if uses' input in the range of stardard card
#         print('Out of card range. Please check again.')
#         a=int(input("Please input the values of card face(1~13):")) #if not in to loop til in the range
#         b=input("Please input the suit of card (Clubs=C, Diamonds=D, Spades=S, Hearts=H):")
        
#     test=Card(a,b)
#     test2=Card(1,'H')
#     print(test)
#     print(test2)

# if __name__ == '__main__':
#     main()

