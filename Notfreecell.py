#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from deck import Deck

class NotFreecell:
    valid_group = ["c1", "c2", "c3", "c4", "f1", "f2", "f3", "f4", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]

    
    # constructor
    # use deck as initial function
    # deck.get_deck()= deck ex Deck(1, 13,4)=deck=card face from 1 to 13 in 4 suits.
    # for loop:
    # from index=0 to index=7 (there are 8 piles)
    # add card from pile[0] then pile[1] pile[2] .... to pile[7] and loop again from pile[0] to pile[7] till no card in deck.
    def __init__(self, deck:Deck):
        self.piles = [[], [], [], [], [], [], [], []]
        self.cells = [[], [], [], []]
        self.foundations = [[], [], [], []]
        self.mapping={"p": self.piles, "c": self.cells, "f": self.foundations}
        i = 0
        for card in deck.get_deck():
            self.piles[i].append(card)
            i += 1
            if i == len(self.piles): # when len(piles)=8, i=0 -> back to index=0 (since the last index is 7)
                i = 0
        self.print_rule()
    
    # to represent the game rule and the usage to nagaviate how to play game
    def print_rule(self):
        print("──────────────────────", "Game Rules", "──────────────────────")
        print("Win:")
        print("All cards from 4 suits are moved to their Foundation piles")
        print("Move Rules:")
        print("1. Only one card(top card) can move at a time")
        print("2. Any card may be move to empty Cell")
        print("3. Card moves to Foundation must in ascending order, starting from Ace to King")
        print("4. Card moves from Piles or Cells to another Piles must in the opposite colour and in decending order")
        print("    ie: red 2 can be placed black 3 which in different Pile")
        print("5. Cards in Foundations cannot move back to Pile")
        print("──────────────────────", "Usage", "─────────────────────────")
        print("Make a move (src: source index, dst:destination index):")
        print("Move from Pile_src to Foundations_dst:mv p0 f0 (From p0 to f0 )")
        print("Move from Cell_src to Pil_dst:             mv c1 p2 (From c1 to p2)")
        print("Move from Pile_src to Pile_dst:            mv p1 p3 (From p1 to p3)")
        print("Move from Foundation_src to Cell_dst:  mv f2 c1 (From f2 to c1)")
        print("Move from Foundation_src to Pile_dst:  mv f1 p1  (From f1 to p1)")
        print("Exit game:                                    exit ")
        print("Show Game Rules and Usage:         help")
        print("───────────────────────────────────────────────────")
    
    # to represent the game and its status
    def show_status(self):
        print("─" * 50)  # print design to look clear
        print("Cells")
        for i, card in enumerate(self.cells):# c:cells format: c{i+1}: {card} ex: c2: [9♥️ ]  i=index from 0 to 3 and card which in the cells[i]
            print(f"c{i+1}:{card} ", end="") # since define each cell name from 1 to 4 (c1 c2 c3 c4)-> c1=cells[0]
        print("") # to let "Foundations" print into the next line

        print("Foundations")
        for i, card in enumerate(self.foundations):
            if len(card) != 0:                              # when there is a card in foundation:
                print(f"f{i+1}:[{card[-1]}] ", end="") # f:foundations format: f{i+1}:{card[-1]} i=index from 0 to 3 (foundations[0]=f1=format: f{0+1})
                                                                # card[-1]: only print the top card in foundation[i] ex: [A♥️ 2♥️] -> only print 2♥️
            else:
                print(f"f{i+1}:{card} ", end="")       # if there is no card inside foundation list ex f1:[ ]
        print("")                                            # let "*" print into the next line

        print("*" * 40)                                   # print design to look clear
        print("Piles")
        for i, card in enumerate(self.piles):      # p:piles format p{i+1}:{card} ex p2: [2♥️] p2=piles[1] index from 0 to 7
            print(f"p{i+1}: {card} ")
        print("─" * 50)                                 # print design
    
    # get_group to map group's type and its index
    # ex: group_type=p num=3 nickname=p3 ->p, self.mapping[p][2]=piles[2]
    def get_group(self, nickname):
        group_type, num=nickname
        return group_type, self.mapping[group_type][int(num)-1]


#         Logic:
#         1.If cell is empty, any card can move in
#         2.The card in the foundations is not allow move back to the piles
#         3.If there is a card in the cell, not allow adding other card
#         4.If the foundation is empty, can only join Ace in any suit
#         5.If there are one or more cards inside the foundation, can only add higher value card in the same suit
#         6.If the pile is empty, can add card in
#         7.If there are cards inside pile, can only add lower value card in the opposite colour
#         8.Always can only move the top card.

#         Name:
#         group == pile, cells, foundations
    def move(self, src, dst):
        
        # src->source dst->destination
        src_type, src_group = self.get_group(src) # ex: p3 src_type=p scr_group=self.mapping[p][int(3)-1]=piles[2]
        dst_type, dst_group = self.get_group(dst)
        
        # logic 1
        if len(src_group) == 0: # if pick up the empty source
            return False, "Source pile is empty" # return False and warning
        src_top_card = src_group[-1] # (if pick up the source is not empty) else: the top card of the source= the last card[-1] in the list
        
        # logic2
        if src_type == "f" and dst_type == "p": # if user pick up the card to move from foundation to piles
            return False, "Card from the foundation can not be placed back to any piles" #cannot move since the rule, return False and warning

        # logic 3
        if dst_type == "c": # if the destination is cell
            if len(dst_group) != 0: # if the cell is not empty
                return False, "Only one card at a time can be occupied in a cell" # return False and warning

        # logic 4
        if dst_type == "f": # if the destination is foundation
            if len(dst_group) == 0: # if the foundation is empty
                if src_top_card.card_face != 1: # if the top card from the source is not Ace
                    return False, "Only Ace can be placed in an empty foundation" # return False and warning
            else: # else if the foundation is not empty
                dst_top_card = dst_group[-1] # the top of the chosen foundation = dst_group[-1], dst_group=f, [-1]=the top card(last one in the list)
                if src_top_card.card_suit != dst_top_card.card_suit: # check the suit: need to be the same suit in the foundation
                    return False, "Not the same suit" # if not the same: return False and warning
                if src_top_card.card_face - dst_top_card.card_face != 1: # check :the card from source must one value higher than the card in foundation
                    return False, "Need to follow the ascending order" # ex: 8-6!=1: return False and warning

        # logic 6 7 
        if dst_type == "p": # if pick up the card from the pile
                if len(dst_group) == 0: # logic6: when the pile is empty
                    dst_group.append(src_group.pop()) # add card into the pile (no limitation about which card)
                    return True,"All good" # return True and comment
                if len(dst_group) != 0: # logic7: when the pile is not empty
                    dst_top_card = dst_group[-1] # the top card of the pile = pile[-1]
                    if src_top_card.card_face > dst_top_card.card_face: # check order: source card must one value lower than the card in the pile
                        return False, "Need to the follow descending order" # ex: source 8>6 destination return False and warning
                    if dst_top_card.card_face-src_top_card.card_face!=1: # check oreder as the logic as above (even in descending order):
                        return False,"Need to follow the order" # ex: 5 cannot place into the pile which the top card's value is 7
                    # define suits' colour in order check logic7: add card in the opposite colour
                    black_suit = ["S", "C"] #black:C:♣️, S:♠️ 
                    red_suit = ["H", "D"] #red: H:♥️, D:♦️
                    if (src_top_card.card_suit in black_suit and dst_top_card.card_suit in black_suit) or (
                        src_top_card.card_suit in red_suit and dst_top_card.card_suit in red_suit): # check if source top card and destination top car are different colour
                        return False, "Must be in the opposite colour" # if the same colour: return False and warning
        
        # if every logics are followed and done checking
        dst_group.append(src_group.pop()) # source top card add into destination list
        return True,"All good" # and return True and comment
    
    #check win function
    def is_win(self): 
        for p in self.piles: # for every piles
            if len(p) != 0: # if there are one or more piles still with cards
                return False # return False since if win: every cards should be placed into foundations
        for c in self.cells: # for every cells
            if len(c) != 0: # if there are one or more cells still with card
                return False # return False, the reason as above
        return True # if len(p)=0 and len(c)=0 return True: win
        
        

# main function
def main():
    game_deck = Deck(1, 13, 4) # use the whole deck of card
    game_deck.shuffle() # to shuffle
    game_deck.display_deck() # display the deck of card which is shuffled

    game = NotFreecell(game_deck) 

    

    while not game.is_win(): # when the game is not checked as win
        print("")  # leave a empty line
        game.show_status() # print the design of text interface
        command = input("Make your move:") # allow users to input their moves

        if command == "exit":  # if users input exit
            print("Bye bye") # do the exit() function
            return 0  # and stop loop
           

        if command == "help":  # if users input help
            game.print_rule() # do the print_rule() function
            continue  # and continue the game(while loop)
        
        # check command-> check string length first then mv command than source command then destination command
        if len(command)!=8: # if the len(command) is not 8 ex: mv->len(command)=2 or mv p1-> len(command)=5
            print("Invalid command.") # not a correct command, so print warning message
        else: # if the command is correct ex: command=mv p1 c1 len(mv p1 c1)=8
            mv, src, dst = command.split()# split the commend by space to three strings ex: mv,p1,c1 where mv=mv src=p1 dst=c1
            if mv not in ['mv']: # check if mv command is correct, only accept "mv" as the move command
                print(f"Invalid command, use mv to move") # if wrong print warning message
                continue # and continue loop
            if src not in game.valid_group: # if command for source not in valid_group ex: mv h1 c1 ->h1 is wrong
                print(f"Invalid source {src}") # print warning message to users that not the correct command since no such source in valid_group
            if dst not in game.valid_group: # if command for destination not in  valid_group ex:mv p1 w1 ->w1 is wrong
                print(f"Invalid destination {dst} ") # print warning message that command for destination is wrong
                continue # and continute to loop

            result, reason = game.move(src, dst) # if all command right, result=the result in move()  every logic :True or False
            if result: # if True:
                print(f"{reason}, move {src} to {dst}") # print "All good, move {source command} to {destination command} ex: All good, move p1 to c1
            else: # if False:
                print(f"Warning: {reason}") # print Warning:{reason} where reason is from move() when return False,{reason}
                
    while game.is_win(): # when the game check as win:
        print("♪───Ｏ（≧∇≦）Ｏ────♪##YOU WIN##♪───Ｏ（≧∇≦）Ｏ────♪")
        return 0 # jump out from the loop



if __name__ == "__main__":
    main()

