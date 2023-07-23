words_list = ["hello", "hey", "goodbye", "yo", "yes", "easy"]

for word in words_list:
    print(word.upper())


def words_to_uppercase(words):
    """a function to print all strings inside of a list of strings to uppercase"""
    for word in words:
        print(word.upper())


def e_words_to_uppercase(words):
    """a function to print only strings that start with "e" inside of a list of strings to uppercase"""
    for word in words:
        if word[0] == "e":
            print(word.upper())

def specific_words_to_uppercase (words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word)


words_to_uppercase(words_list)
e_words_to_uppercase(words_list)
specific_words_to_uppercase(words_list, must_start_with={"h", "y"})