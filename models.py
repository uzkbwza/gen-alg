#!/usr/bin/python
from copy import copy
from pprint import pprint
import random

import selections
import mutations

class Model:
    """
    Contains and processes a population of individuals.
    """

    def __init__(self, pop_size=50, dna=[], gene_length=0, elites=3, mutation_probability=5,crossover_probability=50):
        self.pop_size = pop_size
        self.dna = dna
        self.gene_length = gene_length
        self.population = []
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.elites = elites
        self._selection_method = selections.roulette
        self._mutation_method = mutations.simple
    
    def set_fitness_method(self, funct):
        self._fitness_method = funct

    def set_selection_method(self, funct):
        """Try to use the selection methods from the selections module,
        unless you really know what you're doing."""
        self._selection_method = funct

    def evaluate(self,population):
        if not self._fitness_method:
            raise Exception(
                    "A fitness evaluation function is needed to evaluate fitness!" \
                    "Please create and set one using set_fitness_method.")
        for individual in population:
            individual.fitness = self._fitness_method(individual)
        self._sort(population)

    def populate(self):
        """Randomly generates individuals to fill new population"""
        self.population = [self._generate_individual() for i in range(self.pop_size)]
        self.generation = 0
        print("Created random population")

    def breed(self,parent_a,parent_b):

        new_chromosome = random.choice([parent_a.chromosome,parent_b.chromosome])
        if random.randint(0,100) < self.crossover_probability:
            new_chromosome = []
            crossover_point = random.randint(0,self.gene_length)
            for i in range(self.gene_length):
                new_chromosome.append(random.choice([parent_a.chromosome[i],parent_b.chromosome[i]]))
        child = self._generate_individual()
        child.chromosome = new_chromosome.copy()
        child._mutation_method(child)
        return child

    def select(self):
        """Select individuals to pass on their chromosome to the next generation
        using method defined in set_selection_method"""
        
        current_gen = self.population
        next_generation = [] 

        # Make sure the fittest of last generation cross through
        if self.elites: 
            next_generation.extend(current_gen[-self.elites:])
            # pprint(["".join(i.chromosome) for i in next_generation])


        for i in range(self.pop_size - self.elites): 
            parent_a = self._selection_method(current_gen)
            parent_b = self._selection_method(current_gen)
            child = self.breed(parent_a,parent_b)
            next_generation.append(child)

        for individual in next_generation:
            individual.fitness = 1


        return next_generation

    def print_gen(self,pop):
        """Prints information regarding current population"""
        fit_min = pop[0].fitness
        fit_max = pop[-1].fitness
        fit_avg = sum([individual.fitness for individual in pop]) / len(pop)
        dna = str(pop[-1]).encode()


        format_tuple = (
            self.generation,
            fit_min,
            fit_max,
            fit_avg,
            "".join(pop[-1].chromosome))

#        pprint([["".join(i.chromosome),i.fitness] for i in self.population][-15:])
        print("Generation {0:<5} ║ Fit Max/Min/Avg: {2:<5.1f} / {1:^5.1f} / {3:>5.1f} ║ \nChromosome: {4}\n".format(*format_tuple))
        
    
    def process(self,max_fitness,interval):
        """Main loop. Evaluates fitness, checks if max fitness has been reached
        and returns the best individual if so, selects the next populations,
        and iterates the generation count."""

        # Main loop
        while True:
            self.evaluate(self.population)
            best = self.population[-1]
            if best.fitness >= max_fitness:
                return best

            # show information of current gen
            if self.generation % interval == 0 and self.generation >= 1:
                self.print_gen(self.population)

            self.population = self.select()
            self.generation += 1
       
    def run(self,max_fitness=None,interval=10):
        "2"
        if not self.population:
            self.populate()
        self.print_gen(self.population)
        try:
            self.process(max_fitness,interval)
        except KeyboardInterrupt:
            print("Interrupted...")
        
        self.print_gen(self.population)
        
        return self.population 

    def _sort(self,pop):
        pop.sort(key=lambda individual: individual.fitness) 
        return pop

    def _generate_individual(self):
        """Randomly generates individual"""
        chromosome = [random.choice(self.dna) for i in range(self.gene_length)]
        individual = Individual(chromosome,self.dna)
        individual._mutation_method = self._mutation_method
        individual.mutation_probability = self.mutation_probability
        individual.crossover_probability = self.crossover_probability
        return individual


class Individual:
    """
    Contains a chromosome and a fitness.
    """
    def __init__(self, chromosome, dna, fitness=0):
        self.fitness = fitness
        self.chromosome = chromosome
        self.dna = dna
        self.evaluated = False

    def __repr__(self):
        return "{}".format("".join(self.chromosome),self.fitness)
    

