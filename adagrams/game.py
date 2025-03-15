import random

# constants
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# HELPER FUNCTIONS
# creates a pile of all available letters (a list) for future correct distribution probability purposes
def create_a_pile_of_letters():
    pile_of_packed_letters = []
    string_pile = ""
    pile_of_unpacked_letters = []

    for letter, number in LETTER_POOL.items():
        pile_of_packed_letters.append(letter * number)
    
    string_pile = "".join(pile_of_packed_letters)
    pile_of_unpacked_letters = list(string_pile)

    return pile_of_unpacked_letters

# MAIN LOGIC
# draw 10 letters from the pile randomly, remove chosen letter from pile
def draw_letters():
    pile_of_letters = create_a_pile_of_letters()
    hand = []

    for letter in range(10):
        letter = pile_of_letters.pop(random.randint(0, len(pile_of_letters))-1)
        hand.append(letter)
    
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass