from queue import PriorityQueue

def greedy_bfs(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))
    
    while not pq.empty():
        (cost, node) = pq.get()
        
        if node == goal:
            return cost
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                pq.put((heuristic(neighbor, goal), neighbor))
                
    return float('inf') # no path found

def heuristic(node, goal):
    # Manhattan distance between two points
    (x1, y1) = node
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)
