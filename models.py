#!/usr/bin/python
import random
from time import sleep
import numpy as np
from pprint import pprint

class Model:
    """
    Contains a population of individuals.
    """

    def __init__(self, length, gene_candidates=[], gene_length=0, mutation_probability=10, mutation_amount=10):
        self.length = length
        if length < 5:
            raise Exception("Generation length must be >= 5")
        self.gene_candidates = gene_candidates
        self.gene_length = gene_length
        self.population = []
        self.generation = 1
        self.mutation_probability=mutation_probability
        self.mutation_amount=mutation_amount
        self.create_first_population() 

    def create_first_population(self):
        self.population = [self._create_individual() for i in range(self.length)]
        print("Created random population")
#        for individual in self.population:
#            print(individual.genes, individual.fitness)

    def get_best_individual(self):
        self.fit_sort()
        return self.population[0]

    def next(self):
        """Breed individuals chosen by roulette to populate next generation"""

        self.fit_sort()

        # 1/10 of next generation will be randomly created
        num_random_creations = 10 *  self.length // 100
        if num_random_creations == 0:
            num_random_creations = 1

        random_individuals = [self._create_individual() for i in range(num_random_creations)]
        
        fitness_sum = sum([individual.fitness for individual in self.population])

        # Best individual from last generation is kept,
        # as well as a child of the best and third best,
        # and a few completely random individuals
        next_generation = [self.population[0],self.breed(self.population[0],self.population[2])]
        for i in range(self.length - 2 - num_random_creations):
            parents = []
            for i in range(2): parents.append(self._exponential_rank_selection())
            next_generation.append(self.breed(parents[0],parents[1]))
        
        next_generation.extend(random_individuals)
        self.population = next_generation
        self.generation += 1
        
    def breed(self,individual_A,individual_B):

        child = individual_A.breed(individual_B,self.gene_candidates,self.mutation_probability,self.mutation_amount)
        return child

    def _roulette_selection(self,fitness_sum):
        """not currently being used"""
        selection = random.random() * fitness_sum
        loop_sum = 0
        for individual in self.population:
            loop_sum += individual.fitness
            if loop_sum >= selection:
                return individual

    def _exponential_rank_selection(self):
        self.fit_sort()
        rank_dict = {} 
        pop_list = self.population
        pop_list.reverse()

        for i, individual in enumerate(self.population):
            rank = i
            rank_dict[individual] = rank
        rank_sum = sum(rank_dict.values())
        selection = random.random() * rank_sum
        loop_sum = 0

        for individual, ranking in rank_dict.items(): 
            loop_sum += ranking
            if loop_sum >= selection:
                return individual
            


    def fit_sort(self):
        self.population.sort(key=lambda individual: individual.fitness, reverse=True)
        for individual in self.population:
            if individual.fitness < 1: 
                individual.fitness = 1

    def _create_individual(self):
        """Randomly generates individual"""

        genes = [random.choice(self.gene_candidates) for i in range(self.gene_length)]
        individual = Individual(genes)
        return individual


class Individual:
    """
    Contains a chromosome and a fitness.
    """
    def __init__(self, genes, fitness=1):
        self.fitness = fitness
        self.genes = genes
    
    def breed(self,other,gene_candidates,probability=10,amount=10):
        child = self.crossover(other)
        child.mutate(gene_candidates,probability,amount)  
        return child

    def crossover(self, other):
        """Create new chromosome from 2 parents"""
        
        new_genes = [random.choice([self.genes[i],other.genes[i]]) for i in range(len(self.genes))]
        return Individual(new_genes)

    def mutate(self,gene_candidates,probability,amount):
        """Randomly change some genes"""
        if random.randint(0,100) <= probability:
           amount = (random.randint(0,amount) * len(self.genes)) // 100
           if amount <= 1: 
               amount = 1
           indices = random.sample(range(len(self.genes)), amount)
           for i in indices:
               self.genes[i] = random.choice(gene_candidates)
