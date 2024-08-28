from math import inf
def divide(first = 1, second = 1):
    if second == 0:
        if first > 0:
            return(float('inf'))
        else:
            return (float('-inf'))
    else:
        return(first/second)
