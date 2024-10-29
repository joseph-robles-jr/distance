import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path, current_node = [], end
    while shortest_path[current_node] is not None:
        path.append(current_node)
        current_node = shortest_path[current_node]
    path.append(start)
    path.reverse()
    
    return path, distances[end]

# Example graph structure with US states. The node is on the left, the distance to defined nodes in on the right.
# Repace structure with grad plan details.
graph = {
    'WA': {'OR': 160, 'ID': 619}, 
    'OR': {'WA': 160, 'CA': 535, 'NV': 663, 'ID': 441},

}


start_node = 'CA'
end_node = 'ME'
path, distance = dijkstra(graph, start_node, end_node)

print(f"Shortest path:\n {path}")
print(f"Total distance: {distance}")
