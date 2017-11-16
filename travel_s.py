#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genetica Algorithm that tackles the 
Travelling salesman problem

Created on Tue Nov 14 14:34:39 2017

@author: pesa
"""

import population as pop
import numpy as np
import pandas as pd

# read in a table containing the distances between cities
distances_df = pd.read_csv('distances.csv', index_col=0)

# define custom fitness function:
# 1 - get an array of cities represented as numbers
# 2 - lookup on the distance table the distance between
# each pair of city in the sequence
# 3 add al the distances together
def get_tot_dist(order_of_cities_visited):
    tot_dist = 0
    for i in range(0, len(order_of_cities_visited)-1) :
        # get the 1st city by checking what number we have at each position
        # in the array of cities == our genotype
        city1 = order_of_cities_visited[i]
        city2 = order_of_cities_visited[i+1]
        tot_dist += distances_df.iloc[(city1,city2)]
    arbitrary_big_negative = -10000
    return arbitrary_big_negative - tot_dist

# initialise a pupulation with 100 agents,
# each with a genotype of length 8,
# then pass in the fitness function we've just defined
p = pop.Population(10, 8, get_tot_dist) 


#agent1, agent2 = p.crossover(p.members[3], p.members[4])

for i in p.members:
    print(i.genotype)

print("-------")    
p.next_gen(1)

for i in p.members:
    print(i.genotype)
for i in range (0, 5): 
    print(p.evaluate()[0].fitness)
    print(p.evaluate()[-2].fitness)
    print('------')