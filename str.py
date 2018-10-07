#!/usr/bin/python
from models import *
import string
import timeit

# PASSWD = input("Give passwd: ")
PASSWD = "____________________________________________"

dna = ["_","a","b","c","1","2","3"]# string.ascii_letters + string.digits + string.punctuation + " " 
gene_length = len(PASSWD)
pop_size = 100
elites = 30

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

model = Model(
        pop_size,
        dna=dna,
        gene_length=gene_length,
        elites = elites
)

model.set_fitness_method(fitness)
start = timeit.default_timer()
model.run(max_fitness=100,interval=1)
print("0")
end = timeit.default_timer()
print(end-start)
