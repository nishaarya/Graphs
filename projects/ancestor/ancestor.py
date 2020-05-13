from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # create a dictionary
    struct = {}

    # Loop through each pair in the ancestor list
    for pair in ancestors:
        # Parent is the first value of pair
        parent = pair[0]
        # Child is the second value of pair
        child = pair[1]

        # If Child is not in 'struct', add it
        if child not in struct:
            struct[child] = []

        # Then add the parents of each child to their list in the dict
        struct[child].append(parent)
    
    # Create a queue
    q = Queue()

    # Append the starting node 
    q.enqueue([starting_node])

    # Set a default longest node to store the largest distance
    # index 0 and the last node - as it corresponds with the longest distance
    longest_node = [0,-1]

    # Check if the queue is empty
    while len(q) > 0:
        # pop the first path from the queue
        curr_path = q.popleft()

        # get the last node in the path 
        last_node = curr_path[-1]

        # Check if the last node is in the dictionary
        if last_node not in struct:
            # if the curr_path is longer than the previous_path, that will be the new longest path
            if len(curr_path) > longest_node[0] and last_node > longest_node[1]:
                # store the new longest_node
                longest_node = [len(curr_path), last_node]
        
        # else, if the last_node does have parents
        else:
            # loop through each parent and queue up
            # a path from the current path to each parent
            for x in struct[last_node]:
                q.append(curr_path + [x])
        
        # if the longest_node is = starting_node, return -1 as the starting_node has no parents
        if longest_node[1] == starting_node:
            return -1

        # Else return the node furthest away, which is longest_node[1]
        else:
            return longest_node[1]


