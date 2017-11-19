#!/usr/bin/env python

"""
Python source code - Code Retreet Code: Conway game of life 
"""
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from numpy.random import randint
import numpy as np
from scipy.ndimage import convolve


def next_state(alive, neighbors):
    logic = {True: {2: 1, 3: 1}, False: {3: 1}}
    return logic[alive].get(neighbors, 0)


def map_row_of_states(alive_row, neighbor_row):
    return map(next_state, alive_row, neighbor_row)

def map_grid(alive_grid, neighbor_grid):
    return map(map_row_of_states, alive_grid, neighbor_grid)

class Board(object):
    def __init__(self, rows, cols, dep):
         self.dims = (rows, cols, dep)
         self.grid = np.zeros((rows, cols, dep))

    def set_random(self):
         self.grid = randint(2, size=self.dims)

    def next_iter(self):
         kernel = np.ones((3, 3, 3)) # create a kernal
         kernel[1][1][1] = 0         # set center kernal = 0
            #        convol passes grid and kernal under constant mode
            #        to scan space and return vales to test the state 
         neighbors = convolve(self.grid, kernel, mode='constant')
         new_state = map(map_grid, self.grid, neighbors)
         new_state = np.array(new_state)
         self.grid = new_state

    def __repr__(self):
         return str(self.grid)

def run_random_board():
    board = Board(3, 3, 3)
    board.set_random()
    print(board)
    board.next_iter()
    print(board)


if __name__ == '__main__':
    run_random_board()
