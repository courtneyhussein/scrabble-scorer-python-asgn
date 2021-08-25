# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85
#import string

OLD_POINT_STRUCTURE = {
  0: [' '],
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   word = ''
   while not ((word.replace(" ", "")).isalpha()):
       word = input('Enter a word to score: ')
   return word


def simple_scorer(word):
   return f'Simple Scorer - {word} is worth: {len(word)} points'

def vowel_bonus_scorer(word):
    word_score = 0
    vowels = 'aeiou'
    for char in word.lower():
        if char in vowels:
            word_score += 3
        else:
            word_score += 1
    return f'Vowel Bonus Scorer - {word} is worth: {word_score} points' 

def scrabble_scorer(word):
    word_score = 0
    for char in word.lower():
        word_score += new_point_structure[char]
    return f'Scrabble Scorer - {word} is worth: {word_score} points'

scoring_algorithms = (
    {'Name': 'Simple Score',
    'Description': 'Each letter is worth 1 point.',
    'Score Function': 'A function with a parameter for user input that returns a score.'},
    {'Name': 'Bonus Vowels',
    'Description': 'Vowels are 3 pts, consonants are 1 pt.',
    'Score Function': 'A function that returns a score based on the number of vowels and consonants.'},
    {'Name': 'Scrabble',
    'Description': 'The traditional scoring algorithm.',
    'Score Function': 'Uses the old_scrabble_scorer() function to determine the score for a given word.'}
)

def scorer_prompt(word):
    selection = input('''Which scoring algorithm would you like to use? \n
    0 - Simple: One point per character
    1 - Vowel Bonus: Vowels are worth 3 points
    2 - Scrabble: Uses scrabble point system
    Enter 0, 1, or 2\n''')
    selection = int(selection)
    if selection == 0:
        print(simple_scorer(word))
    elif selection == 1:
        print(vowel_bonus_scorer(word))
    elif selection == 2:
        print(scrabble_scorer(word))
    return scoring_algorithms[selection]
        
def transform(old_dict):
    new_dict = {}
    for key in OLD_POINT_STRUCTURE:
        for letter in OLD_POINT_STRUCTURE[key]:
            new_dict[letter.lower()] = key
    return new_dict

new_point_structure = transform(OLD_POINT_STRUCTURE)

def run_program():
    word = initial_prompt()
    scorer_prompt(word)
