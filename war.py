# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:39:40 2018

@author: arjunb
"""

import random, time

def main():
    
    card_to_value = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':11, 'Q':12, 'K':13, 'A':14}
    #Create a deck of cards
    cards = [x for x in range(2,15)] * 4
    cards = ['A' if x == 14 else 'K' if x == 13 else 'Q' if x == 12 else 'J' if x == 11 else x for x in cards]
    
    #Shuffle the cards and deal
    random.shuffle(cards)
    player_1_cards = cards[::2]
    player_2_cards = cards[1::2]
    
    assert len(player_1_cards) == len(player_2_cards)
    
    rounds = 0
    #Play War with a loop
    while len(player_1_cards) > 0 and len(player_2_cards) > 0:
        
        rounds += 1
        print("\nPlayer 1: "),
        card1 = player_1_cards.pop(0)
        print(card1)
        print("Player 2: "),
        card2 = player_2_cards.pop(0)
        print(card2)
        
        if card_to_value[card1] > card_to_value[card2]:
            print("Player 1 wins")
            player_1_cards.extend([card1, card2])
            
        elif card_to_value[card2] > card_to_value[card1]:
            print("Player 2 wins")
            player_2_cards.extend([card2, card1])
    
        else:
            print("Tie! We go to war!")
            face_down_1 = [card1]
            face_down_2 = [card2]
            
            while card_to_value[card1] == card_to_value[card2]:
                if len(player_1_cards) < 4:
                    face_down_1.extend(player_1_cards)
                    player_2_cards.extend(face_down_2 + face_down_1 + player_1_cards)
                    player_1_cards.clear()
                    break
                elif len(player_2_cards) < 4:
                    player_1_cards.extend(face_down_1 + face_down_2 + player_2_cards)
                    player_2_cards.clear()
                    break
                
                print("\nPlayer 1 3 cards face down")
                print("Player 2 3 cards face down")
                for i in range(3):
                    face_down_1.append(player_1_cards.pop(0))
                    face_down_2.append(player_2_cards.pop(0))
            
                print("War Card Player 1: "),
                card1 = player_1_cards.pop(0)
                face_down_1.append(card1)
                print(card1)
                print("War Card Player 2: "),
                card2 = player_2_cards.pop(0)
                face_down_2.append(card2)
                print(card2)
                
                if card_to_value[card1] > card_to_value[card2]:
                    print("Player 1 wins")
                    player_1_cards.extend(face_down_1 + face_down_2)
                elif card_to_value[card2] > card_to_value[card1]:
                    print("Player 2 wins")
                    player_2_cards.extend(face_down_2 + face_down_1)
                
                time.sleep(5)
        
        print("\nPlayer 1 card count: " + str(len(player_1_cards)))
        print("Player 2 card count: " + str(len(player_2_cards)))
        assert len(player_1_cards) + len(player_2_cards) == 52
        #input()
        time.sleep(5)
        
    if len(player_2_cards) == 0:
        print("\nPlayer 1 wins the game!")
    elif len(player_1_cards) == 0:
        print("Player 2 wins the game!")
    print("\nLength of game: " + str(rounds) + " rounds")
        

if __name__ == "__main__":
    main()