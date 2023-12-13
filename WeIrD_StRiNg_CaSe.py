'''
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
'''


def to_weird_case(words):
    weird_words = []
    for word in words.split():
        weird_word = ''
        for i, ch in enumerate(word):
            if i % 2 == 0:
                weird_word += ch.upper()
            else:
                weird_word += ch.lower()
        weird_words.append(weird_word)
    return ' '.join(weird_words)


print(to_weird_case('String'))
print(to_weird_case('Weird string case'))
