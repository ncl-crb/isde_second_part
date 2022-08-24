"""
Give a list of integers, find the nearest pair that sum to a given target. Nearest refers to the position in the list.
"""

#

def nearest(list, target):
    for dist in range(1, len(list)):
        for i in range(len(list) - dist):
            if (list[i] + list[i+dist]) == target:
                return (list[i], list[i+dist]), i, i + dist, dist
        dist +=1
    return (None, None), None, None, None


list = [1, 5, 3, 6, 4, 2]

target = 3
dist = 0

items, idx1, idx2, dist = nearest(list, target)
print(f"items: {items} \ndistance: {dist} \nindexes: {idx1} - {idx2}")

#########################################################################

elements = [1, 2, 3, 4]
targets = [0, 3, 4, 5, 6, 7]
solution = [(None, None), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]

print(f"Test from Didaci:\n")

for i in range(len(targets)):

    print('\ntarget: ', targets[i])

    #idx_0, idx_1 = idx_sum_is(elements, targets[i])
    _, idx_0, idx_1, _ = nearest(elements, targets[i])

    if idx_0 is None:
        print('target ', targets[i], ': no solution\n')
    else:
        print('POSITIONS (', idx_0, idx_1, '):', elements[idx_0], '+', elements[idx_1], ' = ',
              elements[idx_0] + elements[idx_1])

    if (solution[i][0] != idx_0) or (solution[i][1] != idx_1):
        raise ValueError("Problems in your code!!")
