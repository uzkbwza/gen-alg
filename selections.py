import random
import numpy as np
from collections import OrderedDict 
from pprint import pprint

def roulette(model):
    fitness_sum = sum([individual.fitness for individual in model.population]) 
    selection = random.random() * fitness_sum
    loop_sum = 0
    for individual in model.population:
        loop_sum += individual.fitness
        if loop_sum >= selection:
            return individual

def linear_rank(model):
    rank_dict = OrderedDict()
    pop_list = model.population
    for i, individual in enumerate(model.population):
        rank = i
        rank_dict[individual] = rank
    rank_sum = sum(rank_dict.values())
    selection = random.random() * rank_sum
    loop_sum = 0
    for individual, ranking in rank_dict.items(): 
        loop_sum += ranking
        if loop_sum >= selection:
            return individual
