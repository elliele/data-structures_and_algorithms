# Created by Ellie Le at 4/13/2021

def find_max(data):
    """Return the maximum element from a nonempty Python list."""
    biggest = data[0]           # The initial value to beat
    for val in data:            # For each value
        if val > biggest:       # if it is greater than the best so far
            biggest = val       # we have found a new best (so far)
    return biggest              # When loops ends, biggest is the max

