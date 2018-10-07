import random

def simple(individual):
    for location in range(len(individual.chromosome)):
        if random.randint(0,100) <= individual.mutation_probability: 
            individual.chromosome[location] = random.choice(individual.dna)

