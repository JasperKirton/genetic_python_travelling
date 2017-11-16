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
    return arbitrary_big_negative + tot_dist

# initialise a pupulation with 100 agents,
# each with a genotype of length 8,
# then pass in the fitness function we've just defined
pop_number = 20
size_of_genotype = distances_df.columns
p = pop.Population(pop_number, size_of_genotype, get_tot_dist) 



# TEST TO SEE WHTHER THE FITNESS INCREASES (and the distance dicreases)

max_gen = 3200 
i=0
while i < max_gen:
    if i % 50 == 0 :
        print('.')
    if(i % 300 == 0) : 
        print('temporary best fitness: ', p.evaluate()[0].fitness, 
              ' distance: ', p.evaluate()[0].fitness+ 10000)
    p.next_gen(3) # keeping the 2 best at the moment (3 couples)
    i+=1
    
print('final best fitness : ', p.evaluate()[0].fitness, ' distance: ', 
              p.evaluate()[0].fitness+10000)