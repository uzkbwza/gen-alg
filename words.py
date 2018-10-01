#!/usr/bin/python
from pprint import pprint
import random
import operator
import string

def fitness(password,test_word):
    """
    Evaluates fitness level based on similarity of input word to given password
    """
    
    if len(password) != len(test_word):
        print("Incompatible sizes")
        return

    score = 0
    
    for i, pass_char in enumerate(password):
        if test_word[i] == pass_char:
            score += 1

    fitness = score * 100 / len(password)

    return fitness 


def gen_word(password):
    """
    Generates random string of characters the same length as password
    """
    
    # Define what characters are available for use in generated words
    available_chars = string.ascii_letters + string.digits + string.punctuation + " " 
    
    # Create list of random ASCII characters
    chars = [random.choice(available_chars) for letter in password]

    # Could have used the list comprehension in the previous line
    # But this way is more readable
    word = "".join(chars)

    return word


