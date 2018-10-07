import random

def simple(individual):
    new_chromosome = individual.chromosome
    for location in range(len(individual.chromosome)):
        if random.randint(0,100) <= individual.mutation_probability: 
            new_chromosome[location] = random.choice(individual.dna)
            individual.chromosome = new_chromosome
