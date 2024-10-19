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

def x_coordinates (list1:list) -> list: # takes in a point made of an x and y value and returns the x value
    list2=[]
    for i in range(len(list1)):
        list2.append(list1[i].x)
    return list2

# Part 3

def are_in_positive_quadrant(list1: list[list[int]]) -> list: # takes in a point made of an x and y value and returns
    # a new list of only the points with all positive values
    list2 = []
    for i in list1:
        if i[0] > 0 and i[1] > 0:
            list2.append(i)
    return list2


# Part 4

def distance (point1:list, point2:list)-> float: # takes in 2 points and returns a euclidian distance of type float
    euc = 0
    euc = ((point2.x - point1.x)**2 + (point2.y - point1.y)**2)**(1/2)
    return euc


# Part 5

def manhattan_distance (point1:list, point2:list) -> float: # takes in 2 points and returns a Manhattan distance of type float
    manDist = (point2.x-point1.x) + (point2.y-point1.y)
    return manDist


# Part 6


