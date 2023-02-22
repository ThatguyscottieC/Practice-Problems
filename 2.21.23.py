# Determine if a word or phrase is an isogram.
# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
# Examples of isograms:
# lumberjacks
# background
# downstream
# six-year-old

word = 'downstream'


def isogram(word):
    letters = []
    word = word.lower()

    for letter in word:
        if letter not in letters:
            letters.append(letter)
        elif letter == " " or letter == '-':
            pass
        else:
            return False
    return True


print(isogram(word))
