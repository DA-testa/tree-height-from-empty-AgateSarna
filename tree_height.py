# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    depths = [-1] * n

    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    def get_depth(node):
        if depths[node] != -1:
            return depths[node]
        if parents[node] == -1:
            depths[node] = 1
        else:
            depths[node] = 1+ get_depth(parents[node])

        return depths[node]
    
    for i in range(n):
        get_depth(i)
    
    max_height = max(depths)
    # Write this function
    #max_height = 0
    # Your code here
    return max_height


def main():

    source= input()
    if source[0] == 'I':
        n = int(input())
        data = input()
        parents = np.array(data.split(), dtype=int)
        max_height = compute_height(n, parents)
        print(max_height)
    elif source[0] == 'F':
        file_name = input()
        if "a" in file_name:
            return
        file_name = 'test/' + file_name
        with open(file_name, 'r') as f:
            n = int(f.readline())
            parents = np.array(f.readline().split(), dtype=int)
        max_height = compute_height(n, parents)
        print(max_height)
    else:
        return


    
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))5
