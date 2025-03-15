import random

# CONSTANTS
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

SCORE_CHART = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K",): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
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

# returns how many times item appears in array
def count_item_repetition_in_array(item_to_count, array):
    count = 0
    for item in array:
        if item == item_to_count:
            count += 1
    return count

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
    word = word.upper()
    for letter in word:
        if (count_item_repetition_in_array(letter, word) != 
            count_item_repetition_in_array(letter, letter_bank)):
            return False
    return True

def score_word(word):
    word = word.upper()
    word_score = 0

    for letter in word:
        for letters, score in SCORE_CHART.items():
            if letter in letters:
                word_score += score

    if len(word) >= 7:
        word_score += 8

    return word_score


def get_highest_word_score(word_list):
    pass