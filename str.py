#!/usr/bin/python
from models import *
import string

PASSWD = input("Give passwd: ")

gene_candidates = string.ascii_letters + string.digits + string.punctuation + " " 
gene_length = len(PASSWD)
mutation_probability = 50
mutation_amount = 90
generations = 10000
pop_size = 50

population = Model(
        pop_size,
        gene_candidates=gene_candidates,
        gene_length=gene_length,
        mutation_probability=mutation_probability,
        mutation_amount=mutation_amount
        )

population.fit_sort()

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


def main():
    while True:
        for individual in population.population:
            test_word = "".join(individual.genes)
            individual.fitness = fitness(PASSWD,test_word)

        population.fit_sort()

        reverse = population.population
        reverse.reverse()
        for individual in reverse:
            print("".join(individual.genes))
        print("Generation {}, max fitness: {}".format(population.generation,population.get_best_individual().fitness)) 

        if population.get_best_individual().fitness != 100:
            population.next()
        else:
            print(population.get_best_individual().genes)
            return

main()
