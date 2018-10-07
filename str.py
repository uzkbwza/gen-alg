#!/usr/bin/python
from models import *
import string
import timeit

PASSWD = input("Give passwd: ")

dna = string.ascii_letters + string.digits + string.punctuation + " " 
gene_length = len(PASSWD)
pop_size = 50
elites = 2

def fitness(individual):
    """
    Evaluates fitness level based on similarity of input word to given password
    """
    test_word = "".join(individual.chromosome)
    
    if len(PASSWD) != len(test_word):
        print("Incompatible sizes")
        return
    score = 0
    for i, pass_char in enumerate(PASSWD):
        if test_word[i] == pass_char:
            score += 1
    fitness = score * 100 / len(PASSWD)
    return fitness 

model = Model(
        pop_size,
        dna=dna,
        gene_length=gene_length,
        elites = elites
)

model.set_fitness_method(fitness)

start = timeit.default_timer()
model.run(max_fitness=100)
end = timeit.default_timer()
print(end-start)
