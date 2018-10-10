import random
import numpy as np
from pprint import pprint

def uniform(parent_a,parent_b):
    child_chromosomes = []
    for i in range(2):
        new_chromosome = []
        chromosome_length = len(parent_a.chromosome)
        for i in range(chromosome_length):
            new_chromosome.append(random.choice([parent_a.chromosome[i],parent_b.chromosome[i]]))
        child_chromosomes.append(new_chromosome)
    return child_chromosomes

def single_point(parent_a,parent_b):
    child_chromosomes = []
    parents = [parent_a,parent_b]
    chromosome_length = len(parent_a.chromosome)
    crossover_point = random.randint(0,chromosome_length)
    for i in range(2):
        child = parents[i].chromosome[:crossover_point] + parents[(i+1)%2].chromosome[crossover_point:]
        child_chromosomes.append(child)
    return child_chromosomes

def two_point(parent_a,parent_b):
    child_chromosomes = []
    parents = [parent_a,parent_b]
    chromosome_length = len(parent_a.chromosome)
    crossover_points = sorted(random.sample(range(0,chromosome_length),2))
    for i in range(2):
        child = []
        parent_index = i
        for n, point in enumerate(crossover_points):
            parent_index = (n + i) % 2
            previous = np.clip(n-1,0,None)
            child += parents[parent_index].chromosome[n-1:point]
        parent_index = (parent_index + 1) % 2
        child += parents[parent_index].chromosome[crossover_points[-1]:]
        child_chromosomes.append(child)
    return child_chromosomes

def k_point(parent_a,parent_b):
    child_chromosomes = []
    parents = [parent_a,parent_b]
    chromosome_length = len(parent_a.chromosome)
    crossover_points = [0] + sorted(random.sample(range(0,chromosome_length),random.randint(2,chromosome_length)))
    for i in range(2):
        child = []
        parent_index = i
        for n, point in enumerate(crossover_points):
            parent_index = (n + i) % 2
            previous = np.clip(n-1,0,None)
            child += parents[parent_index].chromosome[crossover_points[n-1]:point]
        parent_index = (parent_index + 1) % 2
        child += parents[parent_index].chromosome[crossover_points[-1]:]
        child_chromosomes.append(child)
    return child_chromosomes
