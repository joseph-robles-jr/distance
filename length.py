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
# Should be about 3400 when inputer correctly and run.
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
    'KS': {'CO': 536, 'NE': 165, 'MO': 204, 'OK': 293},
    'OK': {'CO': 336, 'KS': 293, 'TX': 388, 'AR': 337, 'NM': 585, 'MO':401},
    'TX': {'NM': 697, 'OK': 388, 'AR': 504, 'LA': 430},
    'MN': {'SD': 258, 'WI': 244, 'ND': 435, 'IA': 244},
    'IA': {'MN': 244, 'SD': 165, 'NE': 195, 'MO': 255, 'IL': 291, 'WI': 279},
    'WI': {'MN': 258, 'MI': 194, 'IL': 249, 'IA': 279},
    'MI': {'WI': 193, 'IN': 244, 'OH': 237},
    'IN': {'MI': 244, 'IL': 190, 'OH': 175, 'KY': 145},
    'IL': {'WI': 249, 'MO': 129, 'IN': 190, 'KY': 415, 'IA': 291},
    'MO': {'NE': 343, 'KS': 204, 'OK': 401, 'AR': 340, 'IL': 129, 'TN': 453, 'KY': 563, 'IA': 255},
    'AR': {'MO': 340, 'OK': 337, 'TX': 504, 'LA': 416, 'MS': 253, 'TN': 344},
    'LA': {'TX': 430, 'AR': 416, 'MS': 150},
    'MS': {'LA': 150, 'AL': 242, 'TN': 392, 'AR': 253},
    'AL': {'MS': 242, 'TN': 282, 'GA': 160, 'FL': 205},
    'GA': {'AL': 160, 'TN': 255, 'FL': 252, 'SC': 212, 'NC': 434},
    'FL': {'GA': 205, 'SC': 252},
    'SC': {'GA': 212, 'NC': 200},
    'NC': {'SC': 200, 'GA': 434, 'TN': 530, 'VA': 156},
    'VA': {'NC': 156,'TN': 597 ,'KY': 597, 'WV': 302, 'MD': 129},
    'KY': {'VA': 597, 'MO': 563, 'IL': 415, 'IN': 145, 'OH': 186, 'WV': 192, 'TN': 203},
    'TN': {'KY': 203, 'VA':597, 'NC': 530, 'MO': 453, 'AR': 344, 'MS': 392, 'AL': 282, 'GA': 255},
    'OH': {'MI': 237, 'IN': 175, 'KY': 186, 'PA': 425, 'WV': 160},
    'WV': {'OH': 160, 'KY': 197, 'VA': 302, 'PA': 354, 'MD': 397},
    'PA': {'OH': 425, 'NY': 268, 'WV': 354, 'DE':124, 'MD': 103, 'NJ': 127},
    'MD': {'PA':103, 'WV': 397,'VA': 129, 'DE': 62},
    'DE': {'MD': 62, 'PA': 124, 'NJ': 108},
    'NJ': {'PA': 127, 'DE': 108, 'NY': 193},
    'NY': {'NJ': 193, 'PA': 268, 'VT': 153, 'MA': 165, 'CT': 111},
    'VT': {'NY': 153, 'MA': 236, 'NH': 106},
    'NH': {'VT': 106, 'ME': 139, 'MA': 68},
    'ME': {'NH': 139},
    'MA': {'NH': 68, 'VT': 236, 'NY': 165, 'CT': 101, 'RI': 45},
    'CT': {'NY':111, 'MA': 101, 'RI': 72},
    'RI': {'CT': 72, 'MA': 45}
}


start_node = 'CA'
end_node = 'ME'
path, distance = dijkstra(graph, start_node, end_node)

print(f"Shortest path:\n {path}")
print(f"Total distance: {distance}")
