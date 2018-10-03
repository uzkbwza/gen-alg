#!/usr/bin/python
from models import *
from words import fitness
import string

PASSWD = input("Give passwd: ")

gene_candidates = string.ascii_letters + string.digits + string.punctuation + " " 
gene_length = len(PASSWD)
mutation_probability = 50
mutation_amount = 90
generations = 10000

population = Model(
        50,
        gene_candidates=gene_candidates,
        gene_length=gene_length,
        mutation_probability=mutation_probability,
        mutation_amount=10
        )

population.fit_sort()


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
