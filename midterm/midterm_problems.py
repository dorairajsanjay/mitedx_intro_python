#MidTerm - Problem 4
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    found = False
    i = 0

    while True:

        temp = base ** i

        if temp > num:
            break

        i += 1

    temp_prev = base ** (i - 1)

    temp_prev_diff = abs(temp_prev - num)
    temp_diff = abs(temp - num)

    if temp_prev_diff > temp_diff:
        return i
    elif temp_prev_diff == temp_diff:
        return i - 1
    else:
        return i - 1


#MidTerm - Problem 5
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    listR = []
    for i in range(0, len(listA)):
        listR.append(listA[i] * listB[i])

    return sum(listR)

#MidTerm - Problem 6
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    temp = list(L)
    for i in range(len(L)):
        # reverse top list
        L[len(L) - 1 - i] = temp[i]

        # reverse inner list
        inL = L[len(L) - 1 - i]
        temp2 = list(inL)
        for j in range(len(inL)):
            inL[len(inL) - 1 - j] = temp2[j]

#MidTerm - Problem 7
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''

    inter_dict = {}
    for i in d1.keys():
        if i in d2.keys():
            inter_dict[i] = f(d1[i], d2[i])

    diff_dict = {}
    for i in d1.keys():
        if i not in inter_dict.keys():
            diff_dict[i] = d1[i]

    for i in d2.keys():
        if i not in inter_dict.keys():
            diff_dict[i] = d2[i]

    return (inter_dict, diff_dict)

#MidTerm - Problem 8
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    temp = list(L)
    for val in temp:

        if not g(f(val)):
            L.remove(val)

    if len(L) > 0:
        return max(L)
    else:
        return -1


flat_list = []

#MidTerm - Problem 9
def flatten(aList, firstTime=True):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    global flat_list

    if firstTime == True:
        firstTime = False
        flat_list = []

    for item in aList:

        if type(item) is list:
            flatten(item, firstTime)
        else:
            flat_list.append(item)

    return flat_list



