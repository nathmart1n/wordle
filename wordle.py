import csv
words = []
with open('wordle_words.csv', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        words = row

guess_one_chars = ['s', 'l', 'e', 't']
guess_one_no_chars = ['a', 'p']
guess_one_chars_not_places = {
    'l': [1, 2],
    'e': [3, 4, 0, 1],
    's': [1, 2, 3, 4],
    't': [0, 1, 2, 3]
}
new_words = []
# guess_one_chars

for word in words:
    if not any([char in word for char in guess_one_no_chars]):
        if all([char in word for char in guess_one_chars]):
            new_words.append(word)
# print(new_words)

acceptable_guesses = []

for word in new_words:
    breaks_letter_placement = False
    for c in word:
        if c in guess_one_chars_not_places.keys() and word.find(c) in guess_one_chars_not_places[c]:
            breaks_letter_placement = True
    if not breaks_letter_placement:
        acceptable_guesses.append(word)


print(acceptable_guesses)

temp = []
vowels = ['u', 'i']

for word in words:
    if all([char in word for char in vowels]):
        if not any([char in word for char in guess_one_no_chars]):
            if all([char in word for char in guess_one_chars]):
                temp.append(word)
# print(temp)
