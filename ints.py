#!/usr/bin/python
from models import *
import string

PASSWD = int(input("Give passwd: "))

gene_candidates = range(-10000,10000)
gene_length = 12
mutation_probability = 50
mutation_amount = 10
generations = 10000

population = Model(
        300,
        gene_candidates=gene_candidates,
        gene_length=gene_length,
        mutation_probability=mutation_probability,
        mutation_amount=10
        )

population.fit_sort()

def fitness(passwd,i):
    difference = abs(sum(i) - passwd)
    average = abs(sum(i) + passwd/2)
    percent_diff = (difference/average)*100
    fitness = 100 - percent_diff
    return fitness

def main():
    while True:
        for individual in population.population:
            individual.fitness = fitness(PASSWD,individual.genes)

        population.fit_sort()

        reverse = population.population
        reverse.reverse()
        for individual in reverse:
            print(individual.genes, sum(individual.genes))
        print("Generation {}, max fitness: {}".format(population.generation,population.get_best_individual().fitness)) 

        if population.get_best_individual().fitness != 100:
            population.next()
        else:
            print(population.get_best_individual().genes)
            return

main()
