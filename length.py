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

# Example graph structure with US states //should be 3400
graph = {
    'WA': {'OR': 160, 'ID': 619}, 
    'OR': {'WA': 160, 'CA': 535, 'NV': 663, 'ID': 441},
    'CA': {'OR': 535, 'NV': 129, 'AZ': 755},
    'ID': {'WA': 619, 'OR': 441, 'MT': 438, 'WY': 727, 'NV': 541, 'UT': 338},
    'MT': {'ID': 438, 'ND': 624, 'SD': 742, 'WY': 675},
    'ND': {'MT': 624, 'SD': 215, 'MN': 435},
    'SD': {'ND': 215, 'MT': 742, 'WY': 455, 'NE': 392, 'MN': 404, 'IA':165},
    'WY': {'ID': 727, 'MT': 675, 'SD': 455, 'CO': 100, 'NE': 444, 'UT': 435},
    'UT': {'ID': 338, 'NV': 534, 'WY': 435, 'CO': 478, 'AZ': 652},
    'NV': {'OR': 663, 'CA': 129, 'UT': 534, 'AZ': 713},
    'AZ': {'CA': 755, 'NV': 713, 'UT': 652, 'NM': 476},
    'NM': {'AZ': 476, 'CO': 355, 'TX': 697, 'OK': 585},
    'CO': {'WY': 100, 'UT': 478, 'NM': 355, 'KS': 536, 'NE': 486, 'OK': 336},
    'NE': {'SD': 392, 'WY': 455, 'CO': 486, 'KS': 165, 'MO': 343},
    # 'KS': {'CO': 536, 'NE': 343, 'MO': 204, 'OK': 401},
    # 'OK': {'CO': 337, 'KS': 401, 'TX': 388, 'AR': 504},
    # 'TX': {'NM': 697, 'OK': 388, 'AR': 430, 'LA': 150},
    # 'MN': {'SD': 258, 'WI': 244},
    # 'WI': {'MN': 244, 'MI': 279, 'IL': 193},
    # 'MI': {'WI': 279, 'IN': 237, 'OH': 245},
    # 'IN': {'MI': 237, 'IL': 190, 'OH': 165, 'KY': 415},
    # 'IL': {'WI': 193, 'MO': 258, 'IN': 190, 'KY': 145},
    # 'MO': {'NE': 291, 'KS': 204, 'OK': 401, 'AR': 344, 'IL': 258, 'KY': 453},
    # 'AR': {'MO': 344, 'OK': 504, 'TX': 430, 'LA': 253, 'MS': 150, 'TN': 344},
    # 'LA': {'TX': 150, 'AR': 253, 'MS': 242},
    # 'MS': {'LA': 242, 'AL': 160, 'TN': 282},
    # 'AL': {'MS': 160, 'TN': 392, 'GA': 160},
    # 'GA': {'AL': 160, 'TN': 255, 'FL': 205, 'SC': 252, 'NC': 434},
    # 'FL': {'GA': 205, 'SC': 212},
    # 'SC': {'GA': 252, 'FL': 212, 'NC': 200},
    # 'NC': {'SC': 200, 'GA': 434, 'VA': 156},
    # 'VA': {'NC': 156, 'WV': 302, 'KY': 597},
    # 'KY': {'VA': 597, 'MO': 453, 'IL': 145, 'IN': 415, 'OH': 197, 'WV': 532, 'TN': 412},
    # 'TN': {'KY': 412, 'MO': 597, 'AR': 344, 'MS': 282, 'AL': 392, 'GA': 255},
    # 'OH': {'MI': 245, 'IN': 165, 'KY': 197, 'PA': 103, 'WV': 160},
    # 'WV': {'OH': 160, 'KY': 532, 'VA': 302, 'PA': 397, 'MD': 62},
    # 'PA': {'OH': 103, 'WV': 397, 'MD': 124, 'NJ': 108},
    # 'MD': {'WV': 62, 'DE': 62},
    # 'DE': {'MD': 62, 'NJ': 108},
    # 'NJ': {'PA': 108, 'DE': 62, 'NY': 111},
    # 'NY': {'NJ': 111, 'PA': 268, 'VT': 165, 'MA': 111},
    # 'VT': {'NY': 165, 'NH': 106},
    # 'NH': {'VT': 106, 'ME': 139, 'MA': 236},
    # 'ME': {'NH': 139},
    # 'MA': {'NH': 236, 'NY': 111, 'CT': 101},
    # 'CT': {'MA': 101, 'RI': 72},
    # 'RI': {'CT': 72, 'MA': 45}
}


start_node = 'CA'
end_node = 'ME'
path, distance = dijkstra(graph, start_node, end_node)

print(f"Shortest path: {path}")
print(f"Total distance: {distance}")
