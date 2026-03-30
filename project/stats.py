def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    for num in data:
        total += num    #add each number in the list to the total
    return round(total / len(data), 2)    # divide total by count, round to 2 decimals


def median(data: list) -> float:
    """
    Calculate median of a list of integers using a for-loop. Assumes data is clean.
    """
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2            #find the middle index of the sorted list
    if len(sorted_data) % 2 == 0:          # even number of items
        return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
    else:                                   # odd number of items
        return round(sorted_data[mid], 2) 


def range(data: list) -> float:
    """
    """
    minimum = data[0]   # assume first item is the smallest
    maximum = data[0]   # assume first item is the largest
    for num in data:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return round(maximum - minimum, 2)  # calculate the range by subtracting minimum from maximum, round to 2 decimals