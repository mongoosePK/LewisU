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
print('Notes: ')

import numpy as np
import queue

class PuzzleState():
    SOLVED_PUZZLE = np.arange(9).reshape((3, 3))

    def __init__(self,conf,g,predState):
        self.puzzle = conf     # Configuration of the state
        self.gcost = g         # Path cost
        self.hcost = self._compute_heuristic_cost()  # Set heuristic cost
        self.fcost = self.gcost + self.hcost
        self.pred = predState  # Predecesor state
        self.zeroloc = np.argwhere(self.puzzle == 0)[0]
        self.action_from_pred = None

    def __hash__(self):
        return tuple(self.puzzle.ravel()).__hash__()

    def _compute_heuristic_cost(self):
        self.fcost = 0
        self.hcost = 0

        zerospot = [0,0]
        zeroloc2 = np.argwhere(self.puzzle == 0)[0]
        self.hcost += abs(zerospot[0]-zeroloc2[0])

        onespot = [0,1]
        oneloc = np.argwhere(self.puzzle == 1)[0]
        self.hcost += abs(onespot[0]-oneloc[0])

        twospot = [0,2]
        twoloc = np.argwhere(self.puzzle == 2)[0]
        self.hcost += abs(twospot[0]-twoloc[0])

        threespot = [1,0]
        threeloc = np.argwhere(self.puzzle == 3)[0]
        self.hcost += abs(threespot[0]-threeloc[0])

        fourspot = [1,1]
        fourloc = np.argwhere(self.puzzle == 4)[0]
        self.hcost += abs(fourspot[0]-fourloc[0])

        fivespot = [1,2]
        fiveloc = np.argwhere(self.puzzle == 5)[0]
        self.hcost += abs(fivespot[0]-fiveloc[0])

        sixspot = [2,0]
        sixloc = np.argwhere(self.puzzle == 6)[0]
        self.hcost += abs(sixspot[0]-sixloc[0])

        sevenspot = [2,1]
        sevenloc = np.argwhere(self.puzzle == 7)[0]
        self.hcost += abs(sevenspot[0]-sevenloc[0])

        eightspot = [2,2]
        eightloc = np.argwhere(self.puzzle == 8)[0]
        self.hcost += abs(eightspot[0]-eightloc[0])

        self.fcost += self.hcost
        return 

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
        """ this function reads the zero location and tests which moves are valid """
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

    def _deepcopy(self, direction):
        copy = PuzzleState(np.array(self.puzzle), self.gcost, self.puzzle)
        copy.action_from_pred = direction
        return copy

    def gen_next_state(self, direction):
        """ This function generates state based on the move """
        newState = self._deepcopy(direction)
        newState.action_from_pred = direction
        zrow, zcol = newState.zeroloc

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
print(f'startstate test:\n{start_state}')
print(f'solved puzzle:\n{start_state.SOLVED_PUZZLE}')
print(f'Frontier Empty? {frontier.empty()}')
print(f'Frontier[0]: \n {frontier.queue[0]}')
print(f'zeroLoc {start_state.zeroloc}')
while not frontier.empty():
    #  choose state at front of priority queue
    next_state = frontier.get()
    num_states = num_states + 1

    #  if goal then quit and return path
    print (f'next state the goal state?{next_state.is_goal()}')
    if next_state.is_goal():
        next_state.show_path()
        break

    # Add state chosen for expansion to closed_set
    closed_set.add(next_state)
    # Expand state (up to 4 moves possible)
    possible_moves = ['up','down','left','right']
    for move in possible_moves:
        if next_state.can_move(move):
            #print(f'{move}')
            neighbor = next_state.gen_next_state(move)
            if neighbor in closed_set:
                continue
            if neighbor not in frontier.queue:
                frontier.put(neighbor)
                print(f'Frontier[0]: \n {frontier.queue[0]}')
            # If it's already in the frontier, it's gauranteed to have lower cost,
            # so no need to update

print('\nNumber of states visited =',num_states)
