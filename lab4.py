import data

# Write your functions for each part in the space below.

# Part 1
def first_element (list1:list[list[int]]) -> list: # takes in a list of nested lists of int and returns a list of just
    # the first element of each nested list
    list1 = [x for x in list1 if x != []]
    list2 = []
    for x in list1:
        a = x[0]
        list2.append(a)
    return list2

# Part 2

def x_coordinates (list1:list[float,float]) -> list: # takes in a point made of an x and y value and returns the x value
    list2=[]
    for x in list1:
        a = x[0]
        list2.append(a)
    return list2

# Part 3


# Part 4


# Part 5


# Part 6


