# gbfspythonexample
Here is an example of Greedy Best-First Search algorithm implemented in Python using a priority queue:
In this example, the graph parameter is a dictionary representing the graph, where each key is a node and the corresponding value is a list of adjacent nodes. The start and goal parameters are the start and goal nodes, respectively.

The greedy_bfs function starts by initializing an empty set of visited nodes and a priority queue, which is used to store the nodes to visit, sorted by their heuristic value. The function then adds the start node to the priority queue with a heuristic value of 0.

In the main loop, the function retrieves the node with the lowest heuristic value from the priority queue, and checks if it is the goal node. If it is, the function returns the total cost of the path to the goal node. Otherwise, the function adds the node to the set of visited nodes, and iterates over its adjacent nodes. For each adjacent node, the function calculates its heuristic value and adds it to the priority queue.

If the priority queue becomes empty, the function returns infinity, indicating that there is no path from the start node to the goal node.

The heuristic function calculates the Manhattan distance between two nodes, which is used to estimate the cost of the path from the current node to the goal node. This heuristic is admissible, meaning that it never overestimates the actual cost of the path.
