import random
import numpy as np
from collections import OrderedDict 
from pprint import pprint

def roulette(pop):
    fitness_sum = sum([individual.fitness for individual in pop]) 
    selection = random.random() * fitness_sum
    loop_sum = 0
    for individual in pop:
        loop_sum += individual.fitness
        if loop_sum >= selection:
            return individual

def linear_rank(pop):
    rank_dict = OrderedDict()
    for i, individual in enumerate(pop):
        rank = i
        rank_dict[individual] = rank
    rank_sum = sum(rank_dict.values())
    selection = random.random() * rank_sum
    loop_sum = 0
    for individual, ranking in rank_dict.items(): 
        loop_sum += ranking
        if loop_sum >= selection:
            return individual
