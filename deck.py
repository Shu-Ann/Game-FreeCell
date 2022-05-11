#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from card import Card

class Deck:
    #make deck as a list
    deck=[] 
    
    ##constructor
    #to set up the initial deck attributes
    #for suits in suit=['C', 'D', 'S', 'H'] (defined in class Card) for 4 types of suit from 'C' to 'H'.
    #for faces in face=[1,2,3,4,5,6,7,8,9,10,11,12,13] (defined in class Card) from 1(value_start-1, since index in the list=0) to 13 
    #creat cards in total number= (value_end-(value_start-1))*number_of_suit
    #join into the deck list
    def __init__(self, value_start, value_end, number_of_suit):
        
        for suits in Card.suit[0:number_of_suit]:
            for faces in Card.face[(value_start-1):value_end]:
                card=Card(faces, suits)
                self.deck.append(card)
        
        self.value_start=value_start
        self.value_end=value_end
        self.number_of_suit=number_of_suit           
    
    #mutators 
    #set up method as the same as above
    def set_deck(self):
        
        for suits in Card.suit[0:self.number_of_suit]:
            for faces in Card.face[(self.value_start-1):self.value_end]:
                card=Card(faces, suits)
                self.deck.append(card)
    
    #accessors
    def get_deck(self):
        return self.deck
    
    #display function: use the card format which set up in class Card to represent and display
    def display_deck(self): 
        print( ' '.join([card.__repr__() for card in self.deck]))
    
    #shuffle function, use random to shuffle
    def shuffle(self):
        random.shuffle(self.deck) 
    
    #add function: give an assigned card(addface, addsuit) and add it into the last(append()) in the deck
    def add_card(self, addface, addsuit):
        self.deck.append(Card(addface, addsuit))
    
    #draw function: pop up the card from the last one(-1) that in the deck
    def draw_card(self):
        return self.deck.pop(-1) 


#uncomment to test

# def main():
#     test_deck = Deck(1,13,1)
#     test_deck.shuffle()
#     test_deck.display_deck()




# if __name__ == "__main__":
#     main()


