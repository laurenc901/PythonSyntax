"""
print words in arg with all uppercase letters
"""


def print_upper_words(words):
    for word in words:
      print(word.upper()) 

"""
print only words that start with "e" or "E"
and uppercase them
"""

def print_e_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper()) 


"""
print only words that start with the given second arg letter
and uppercase them
"""


def print_any_uppercase(words, must_start_with):
     for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


