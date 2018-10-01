#!/usr/bin/python
from pprint import pprint
import random
import operator
import string

POP_SIZE = 100
PASSWD = "What's poppin gamers, it's wqqqqwrt..."

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


def gen_population(pop_size, password):
    """
    Generates population of first generation of random words.
    """
    
    population = [gen_word(password) for individual in range(pop_size)]
    return population


def eval_pop_performance(pop, password):
    """
    Evaluates and ranks population by fitness
    """
    
    pop_performance = {}
    
    for individual in pop:
        pop_performance[individual] = fitness(password, individual) 
    
    return sorted(pop_performance.items(), key=lambda x: x[1], reverse = True)

def select_from_pop(sorted_pop, best_sample, lucky_few):



pop = gen_population(POP_SIZE, PASSWD)
