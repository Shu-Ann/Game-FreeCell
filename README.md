# Game-FreeCell
A simple text form of FreeCell game written by python

## Introduction 
This is my first python project using Object Oriented Design to implement cards, decks and games.
This project produces an interactive text-based FreeCell game where players use given commands to move cards and win the game.

## Game Rule

To Win:
All cards from 4 suits are moved to their Foundation piles
Move Rules:
1. Only one card(top card) can move at a time
2. Any card may be move to empty Cell
3. Card moves to Foundation must in ascending order, starting from Ace to King
4. Card moves from Piles or Cells to another Piles must in the opposite colour and in decending order
    ie: red 2 can be placed black 3 which in different Pile
5. Cards in Foundations cannot move back to Pile

## Command Usage

Make a move (src: source index, dst:destination index):

1. Move from Pile_src to Foundations_dst: mv p0 f0 (From p0 to f0 )
2. Move from Cell_src to Pil_dst:         mv c1 p2 (From c1 to p2)
3. Move from Pile_src to Pile_dst:        mv p1 p3 (From p1 to p3)
4. Move from Foundation_src to Cell_dst:  mv f2 c1 (From f2 to c1)
5. Move from Foundation_src to Pile_dst:  mv f1 p1  (From f1 to p1)
6. Exit game:                             exit 
7. Show Game Rules and Usage:             help

## Text Form 

<img width="457" alt="截圖 2022-05-11 下午4 03 32" src="https://user-images.githubusercontent.com/105199493/167779639-2236d837-7be2-49d3-9279-f6945a382aa1.png">

Run Notfreecell file to play it!
