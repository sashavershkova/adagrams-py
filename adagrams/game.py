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

# creates a pile of all available letters (list)
# for correct distribution probability purposes
def create_a_pile_of_letters():
    pile_of_packed_letters = []
    string_pile = ""
    pile_of_unpacked_letters = []

    for letter, number in LETTER_POOL.items():
        pile_of_packed_letters.append(letter * number)
    
    string_pile = "".join(pile_of_packed_letters)
    pile_of_unpacked_letters = list(string_pile)

    return pile_of_unpacked_letters

# counts how many times item appears in array
def count_item_repetition_in_array(item_to_count, array):
    count = 0
    for item in array:
        if item == item_to_count:
            count += 1
    return count

# finds highest number in array of numbers
def find_highest_number_in_array(array):
    highest_number = 0
    for number in array:
        if number > highest_number:
            highest_number = number
    return highest_number

# finds minimum number in array    
def find_min_in_array(array):
    min_value = array[0]
    for value in array:
        if value < min_value:
            min_value = value
    return min_value


# MAIN LOGIC

# draw 10 letters from the pile randomly
# remove chosen letter from pile
def draw_letters():
    letters_pile = create_a_pile_of_letters()
    hand = []

    for letter in range(10):
        letter = letters_pile.pop(random.randint(0, len(letters_pile))-1)
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
    # create a list of scores corresponding to the word_list
    scores_list = []

    for word in word_list:
        scores_list.append(score_word(word))

    # find the highest score in scores_list
    highest_score = find_highest_number_in_array(scores_list)

    # make a list that contains only words with highest score
    # make a corresponding list that contains len() of these words
    highest_score_words = []
    highest_score_words_len = []

    for index in range(len(scores_list)):
        if scores_list[index] == highest_score:
            highest_score_words.append(word_list[index])
            highest_score_words_len.append(len(word_list[index]))
    
    # set logic for choosing winning word 
    # from the list of words with highest scores
    if len(highest_score_words) == 1:
        win_word = highest_score_words[0]
    else:
        if 10 in highest_score_words_len:
            win_word = highest_score_words[highest_score_words_len.index(10)]
        else:
            win_word_len = find_min_in_array(highest_score_words_len)
            win_word_index = highest_score_words_len.index(win_word_len)
            win_word = highest_score_words[win_word_index]

    win_word_tuple = (win_word, highest_score)

    return win_word_tuple