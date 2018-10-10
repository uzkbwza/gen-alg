#!/usr/bin/python
from models import *
import crossover
import string
import timeit

def fitness(individual):
    """
    Evaluates fitness level based on similarity of input word to given password
    """
    test_word = "".join(individual.chromosome)
    score = 0
    for i, pass_char in enumerate(PASSWD):
        if test_word[i] == pass_char:
            score += 1
    fitness = score  * 100 / len(PASSWD)
    return fitness

PASSWD = "________________________________________________________________________________________"
dna = string.ascii_letters + string.digits + string.punctuation + " " 
chromosome_length = len(PASSWD)
pop_size = 100
elites=10

model = Model(pop_size,dna=dna,chromosome_length=chromosome_length,elites=elites)
model.set_fitness_method(fitness)
model.set_crossover_method(crossover.k_point)
start = timeit.default_timer()
model.run(max_fitness=100,interval=10)
print("0")
end = timeit.default_timer()
print(end-start)
