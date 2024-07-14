#!/bin/python3

import os

def maximumPeople(p, x, y, r):
    town_in_cloud = set()
    pop_in_cloud = [0] * len(y)
    events = []

    # Create events for towns and clouds
    for i in range(len(x)):
        events.append((x[i], (0, i)))  # Town event
    for i in range(len(y)):
        events.append((y[i] - r[i], (-i - 1, 0)))  # Cloud start
        events.append((y[i] + r[i], (i + 1, 0)))  # Cloud end

    # Sort events by position
    events.sort()

    res = 0
    for position, (type, index) in events:
        if type < 0:  # Cloud starts
            cloud_index = -(type + 1)
            town_in_cloud.add(cloud_index)
        elif type > 0:  # Cloud ends
            cloud_index = type - 1
            town_in_cloud.discard(cloud_index)
        else:  # Town event
            town_index = index
            if not town_in_cloud:  # Town is sunny
                res += p[town_index]
            elif len(town_in_cloud) == 1:  # Covered by one cloud
                cloud_index = next(iter(town_in_cloud))
                pop_in_cloud[cloud_index] += p[town_index]

    res += max(pop_in_cloud) if pop_in_cloud else 0  # Max additional population from one cloud removal
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    x = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    y = list(map(int, input().rstrip().split()))
    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)
    fptr.write(str(result) + '\n')
    fptr.close()
