"""
Code defines a Card class and associated functions

This code is adapted from work by Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
which adapts Chapter 18 of _Think Python_, 2ed, by Allen B. Downey for a CS 1110 assignment.
"""

# Translates valid int ranks to names
INT_TO_SUIT = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}

# Translates one-character suit codes to suit ints
SUIT_TO_INT = {'C': 0, 'D': 1, "H": 2, "S": 3}

# Translates valid int ranks to card names (or ranks)
INT_TO_RANK = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
              8: '8', 9: '9', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}

# Translates one-char rank codes to rank ints
RANK_TO_INT = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}

class Card:
    """
    A class to represent playing cards.

    The class has two hidden attributes (only accessible via functions): _suit, and _rank   
    """

    def setSuit(self, value):
        """
        Sets the suit of this card.

        The function throws an AssertionError if the 
        value does not fit the precondition.

        Parameter value: The new suit value
        Precondition: value is an int in INT_TO_SUIT
        """
        
        pass # Write your code here!

    def getSuit(self):
        """
        Returns the suit of this card as an int.
        """
        
        pass # Write your code here


    def setRank(self, value):
        """
        Sets the rank of this card.

        The function throws an AssertionError if the 
        value does not fit the precondition.

        Parameter value: The new rank value
        Precondition: value is an int (key) in INT_TO_RANK
        """

        pass # Write your code here


    def getRank(self):
        """
        Returns the rank of this card, as an int.
        """

        pass # Write your code here


    def __init__(self, suit, rank):
        """
        Initializes a card with given the suit and rank.
        
        The suits and rank are represented as integers.
        
        The possible suits are given as values in INT_TO_SUIT, while 
        the possible ranks are given as values in INT_TO_RANK. If an
        invalid suit and rank are given, the function should throw 
        an AssertionError.
        
        Example: If we execute c = Card(0, 12), then this card is the Queen of
        Clubs, since INT_TO_SUIT[0] is 'Clubs' and INT_TO_RANK[12] is 'Queen'. 
                
        Parameter suit: the suit encoding
        Precondition: suit is an int (key) in INT_TO_SUIT
        
        Parameter rank: the rank encoding
        Precondition: rank is an int (key) in INT_TO_RANK
        """
        
        pass # Write your code here

    
    def __str__(self):
        """
        Returns a readable string representation of this card.
        
        Examples: '2 of Hearts'
                  'Ten of Clubs'
        """

        pass # Write your code here

    
    def __eq__(self, other):
        """
        Returns: NotImplemented if `other` is not a Card.
        Otherwise, returns...
            True if `other` is a Card that has the same suit and rank 
            as this Card; False otherwise. 
        """

        pass # Write your code here


    def __lt__(self, other):
        """
        Returns: True if this card is less than other
        
        Cards are compared according to poker ordering, with Aces high.
        
        Parameter other: the value to compare
        Precondition: other is a Card
        """

        pass # Write your code here


    def __gt__(self, other):
        """
        Returns: True if this card is greater than other
        
        Cards are compared according to poker ordering, with Aces high.
        
        Parameter other: the value to compare
        Precondition: other is a Card
        """

        pass # Write your code here