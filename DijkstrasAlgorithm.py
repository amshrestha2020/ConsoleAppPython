'''Implement Dijkstra's Algorithm'''

print("******* Implementation of Dijkstra's Algorithm **********")

graph = {
'A' : { 'B' : 3, 'C' : 4, 'D' : 7},
'B' : { 'C' : 1, 'F' : 5},
'C' : { 'F' : 6, 'D' : 2},
'D' : { 'E' : 3, 'G' : 6},
'E' : { 'G' : 3, 'H' : 4},
'F' : { 'E' : 1, 'H' : 8},
'G' : { 'H' : 2},
'H' : { 'G' : 2}
}

def DijkstrasAlgorithm(graph, start, end):
    shortest_distance = {}
    track = {}
    unseenNodes = graph
    infinity = 5000
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    'Visit all nodes and check the distance'
    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        'Find the minimum node that are possible to reach the destination.'
        path_options = graph[min_distance_node].items()

        'Calculate the cost each nodes for each path and only update it, if it is lower than the existing distance.'
        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node] :
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]

                track[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    'Calculating the total distance of each nodes from source to destination.'
    currentNode = end
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track[currentNode]
        except KeyError:
            print("Path is not reachable.")
    track_path.insert(0, start)

    if shortest_distance[end] != infinity:
        print("Shortest Distance is :",  str(shortest_distance))
        print("And the path is :",  str(track_path))

DijkstrasAlgorithm(graph, 'A', 'H')