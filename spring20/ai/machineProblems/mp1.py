# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:24:06 2019
Modified on Sat 8 Feb 2020 17:18
@authors: Piotr Szczurek, William Pulkownik

This program implements A* for solving a sliding tile puzzle
"""
print('Artificial Intelligence')
print('MP1: A* for Sliding Puzzle')
print('SEMESTER: Spring 2020')
print('NAME: William Pulkownik')

import numpy as np
import queue

class PuzzleState():
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self,conf,g,predState):
        self.puzzle = conf       # Configuration of the state
        self.gcost = g           # Path cost
        self.hcost = self._compute_heuristic_cost()  # Set heuristic cost
        self.fcost = self.gcost + self.hcost
        self.pred = predState    # Predecesor state
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None

    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__()

    def _compute_heuristic_cost(self):
        hcost = 0
        # find the difference between where the pieces are 
        # and where they should be. I think it might be a little off though
        actual = self.puzzle.ravel()
         for i in range(3):
            for j in range(3):
                x, y = divmod(self.puzzle[i][j], 3)
                hcost += abs(x-i) + abs(y-j)
        return hcost

    def is_goal(self):
        return np.array_equal(PuzzleState.SOLVED_PUZZLE,self.puzzle)

    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)

    def __lt__(self, other):
        return self.fcost < other.fcost

    def __str__(self):
        return np.str(self.puzzle)

    move = 0

    def show_path(self):
        if self.pred is not None:
            self.pred.show_path()
        if PuzzleState.move==0:
            print('START')
        else:
            print('Move',PuzzleState.move, 'ACTION:', self.action_from_pred)
        PuzzleState.move = PuzzleState.move + 1
        print(self)

    def can_move(self, direction):
        # this function reads the zero location and 
        # tests which moves are valid based on its location
        row, col = self.zeroloc

        if row < 2 and direction == 'down':
            return True
        if row > 0 and direction == 'up':
            return True
        if col > 0 and direction == 'left':
            return True
        if col < 2 and direction == 'right':
            return True
        else:
            return False
    # made a function for this because I thought I'd be calling it more
    def _deepcopy(self, direction):
        copy = PuzzleState(np.array(self.puzzle), self.gcost, self.pred)
        copy.action_from_pred = direction
        copy.__init__(copy.puzzle, num_states, next_state)
        return copy

    def gen_next_state(self, direction):
        """ This function generates state based on the move """
        newState = self._deepcopy(direction)
        newState.action_from_pred = direction
        zrow, zcol = newState.zeroloc
        # find new position for zero by incrementing or decrementing
        # then get the element there and swap with the zero
        if direction == 'up' and zrow > 0: 
            row, col = newState.zeroloc.__add__([-1,0])
            num = newState.puzzle[row, col]
            newState.puzzle[row, col] = 0
            newState.puzzle[zrow, zcol] = num
        if direction == 'down' and zrow < 2: 
            row, col = newState.zeroloc.__add__([1,0])
            num = newState.puzzle[row, col]
            newState.puzzle[row, col] = 0
            newState.puzzle[zrow, zcol] = num
        if direction == 'left' and zcol > 0: 
            row, col = newState.zeroloc.__add__([0,-1])
            num = newState.puzzle[row, col]
            newState.puzzle[row, col] = 0
            newState.puzzle[zrow, zcol] = num
        if direction == 'right' and zcol < 2: 
            row, col = newState.zeroloc.__add__([0,1])
            num = newState.puzzle[row, col]
            newState.puzzle[row, col] = 0
            newState.puzzle[zrow, zcol] = num
        return newState
# load random start state onto frontier priority queue
frontier = queue.PriorityQueue()
a = np.loadtxt('mp1input.txt', dtype=np.int32)

start_state = PuzzleState(a,0,None)
frontier.put(start_state)

closed_set = set()
num_states = 0

while not frontier.empty():
    #  choose state at front of priority queue
    next_state = frontier.get()
    num_states = num_states + 1

    #  if goal then quit and return path
    if next_state.is_goal():
        next_state.show_path()
        break

    # Add state chosen for expansion to closed_set
    closed_set.add(next_state)
    # Expand state (up to 4 moves possible)
    possible_moves = ['up','down','left','right']
    for move in possible_moves:
        if next_state.can_move(move):
            neighbor = next_state.gen_next_state(move)
            if neighbor in closed_set:
                continue
            if neighbor not in frontier.queue:
                frontier.put(neighbor)
            # If it's already in the frontier, it's guaranteed 
            # to have lower cost, so no need to update

print('\nNumber of states visited =',num_states)
