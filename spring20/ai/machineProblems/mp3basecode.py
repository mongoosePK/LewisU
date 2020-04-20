#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program checks if there are possible schedules for students for a given
start and finish term, given all constraints.
This works by mapping a term number to each course, given all constraints.
It assigns a negative term number if course is not taken (e.g. elective that is not needed)

ASSUMPTION: term numbers start with 1
"""
import pandas as pd
import numpy as np
from constraint import *

def create_term_list(terms, years=4):
    '''Create a list of term indexes for years in the future'''
    all_terms = []
    for year in range(years):
        for term in terms:    
            all_terms.append(year*6+term)
    return all_terms
    
def map_to_term_label(term_num):
    '''Returns the label of a term, given its number'''
    term_num_to_label_map = {
            0: 'Fall 1',
            1: 'Fall 2',
            2: 'Spring 1',
            3: 'Spring 2',
            4: 'Summer 1',
            5: 'Summer 2',
    }
    if (term_num < 1):
        return 'Not Taken'
    else:
        return 'Year ' + str((term_num - 1) // 6 + 1) + ' ' + term_num_to_label_map[(term_num - 1) % 6]

def prereq(a, b):
    '''Used for encoding prerequisite constraints, a is a prerequisite for b'''
    if a > 0 and b > 0: # Taking both prereq a and course b
        return a < b
    elif a > 0 and b < 0: # Taking prereq a, but not course b
        return True
    elif a < 0 and b > 0: #  Taking course b, but not prereq a
        return False
    else:
        return True # Not taking prereq a or course b

def get_possible_course_list(start, finish):
    '''Returns a possible course schedule, assuming student starts in start term
       finishes in finish term'''
    problem = Problem()
    
    # Read course_offerings file
    course_offerings = pd.read_excel('docs/csp_course_rotations.xlsx', sheet_name='course_rotations')
    course_prereqs = pd.read_excel('docs/csp_course_rotations.xlsx', sheet_name='prereqs')

    # Foundation course terms
    foundation_courses = course_offerings[course_offerings.Type=='foundation']
    for r,row in foundation_courses.iterrows():
        problem.addVariable(row.Course, create_term_list(list(row[row==1].index)))

    """ TODO FROM HERE... """    
    # Core course terms
    core_courses = course_offerings[course_offerings.Type=='core']
    for r,row in core_courses.iterrows():
        problem.addVariable(row.Course, create_term_list(list(row[row==1].index)))

    
    # CS Electives course terms (-x = elective not taken)
    elective_courses = course_offerings[course_offerings.Type=='elective']
    for r,row in elective_courses.iterrows():
        electiveTermList = create_term_list(list(row[row==1].index))
        for i in range(5):
            electiveTermList.insert(0, (i+1)*-1)
        print(electiveTermList)
        problem.addVariable(row.Course, electiveTermList)
    
    # Capstone
    #########
    capstone_courses = course_offerings[course_offerings.Type=='capstone']
    for r,row in capstone_courses.iterrows():
        problem.addVariable(row.Course, create_term_list(list(row[row==1].index)))
    
    # Guarantee no repeats of courses
    ########
    problem.addConstraint(AllDifferentConstraint())
    
    # Control start and finish terms
    #########
    def start_term(a):
        if a>= 0:
            return True
    def finish_by_term(a):
        if a <= 14:
            return True
    for r,row in course_offerings.iterrows():
        problem.addConstraint(start_term, [row.Course])

    for r,row in course_offerings.iterrows():
        problem.addConstraint(finish_by_term, [row.Course])

    # Control electives - exactly 3 courses must be chosen
    ###########
    electiveCourseList = []
    for r,row in elective_courses.iterrows():
        electiveCourseList.append(row.Course)
    

    problem.addConstraint(InSetConstraint([-1,-2,-3,-4,-5]), electiveCourseList)
    problem.addConstraint(SomeInSetConstraint([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]), electiveCourseList)
    
    # Prereqs    
    ########
    prereqList = []
    for r,row in course_prereqs.iterrows():
        prereqList.append(row.prereq)

    coursey = []
    for r,row in course_prereqs.iterrows():
        coursey.append(row.course)

    for i in range(len(prereqList)):
        problem.addConstraint(prereq, [prereqList[i],coursey[i]])
    
    """ ...TO HERE """
    
    # Generate a possible solution
    sol = problem.getSolutions()
    print(len(sol))
    s = pd.Series(sol[0])
    return s.sort_values().map(map_to_term_label)

# Print heading
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: William Pulkownik")

# Check for possible schedules for all start terms
for start in [1]:
    print('START TERM = ' + map_to_term_label(start))
    s = get_possible_course_list(start-1,start+13)
    if s.empty:
        print('NO POSSIBLE SCHEDULE!')
    else:
        s2 = pd.Series(s.index.values, index=s)
        print(s2.to_string())
    print()

