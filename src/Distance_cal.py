from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = {}

    def addEdge(self, src, dest, distance):
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.edges[(src, dest)] = distance
        self.edges[(dest, src)] = distance 

    # A function used by findPaths to print all paths
    def findPathsUtil(self, u, d, visited, path, max_hops, current_hops, all_paths):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d and current_hops <= max_hops:
            all_paths.append(list(path))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            if current_hops < max_hops:
                for i in self.graph[u]:
                    if visited[i] == False:
                        self.findPathsUtil(i, d, visited, path, max_hops, current_hops + 1, all_paths)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def findPaths(self, s, d, max_hops):

        # Mark all the vertices as not visited
        visited = {i: False for i in self.graph}

        # Create an array to store paths
        path = []
        all_paths = []

        # Call the recursive helper function to print all paths
        self.findPathsUtil(s, d, visited, path, max_hops, 0, all_paths)

        return all_paths

    def findPathDistances(self, paths):
        path_distances = []
        for path in paths:
            distance = 0
            for i in range(len(path) - 1):
                distance += self.edges[(path[i], path[i + 1])]  # 使用self.edges代替self.weights
            path_distances.append(distance)
        return path_distances

    def find_avg_distances_for_hops(self, max_hops):
        avg_distances = {}
        for node in self.graph.keys():
            avg_distances[node] = {}
            for target in self.graph.keys():
                if node != target:
                    for hops in range(1, max_hops + 1):
                        paths = self.findPaths(node, target, hops)
                        distances = self.findPathDistances(paths)
                        avg_distance = sum(distances) / len(distances) if distances else 0
                        avg_distances[node][f"{hops} hops to {target}"] = avg_distance
        return avg_distances


g = Graph()

edges = [
    ("Sapporo", "Aomori", 476.2),
    ("Sapporo", "Morioka", 409.8),
    ("Aomori", "Morioka", 178.4),
    ("Aomori", "Akita", 181.9),
    ("Morioka", "Akita", 127.3),
    ("Morioka", "Sendai", 183.5),
    ("Akita", "Yamagata", 211.6),
    ("Sendai", "Yamagata", 61.1),
    ("Akita", "Niigata", 273),
    ("Yamagata", "Niigata", 187),
    ("Sendai", "Fukushima", 79),
    ("Sendai", "Mito", 245.4),
    ("Fukushima", "Niigata", 180.1),
    ("Fukushima", "Utsunomiya", 163.3),
    ("Utsunomiya", "Mito", 95.6),
    ("Mito", "Chiba", 127.5),
    ("Mito", "Omiya", 117),
    ("Utsunomiya", "Omiya", 79.2),
    ("Utsunomiya", "Maebashi", 106.5),
    ("Omiya", "Chiba", 66.1),
    ("Maebashi", "Omiya", 74.7),
    ("Chiba", "Tokyo", 39.2),
    ("Omiya", "Tokyo", 30.3),
    ("Tokyo", "Yokohama", 28.8),
    ("Tokyo", "Hachioji", 47.4),
    ("Hachioji", "Yokohama", 36.5),
    ("Maebashi", "Hachioji", 96.4),
    ("Yokohama", "Shizuoka", 151.4),
    ("Hachioji", "Kofu", 86.7),
    ("Maebashi", "Nagano", 117.4),
    ("Kofu", "Shizuoka", 122.4),
    ("Maebashi", "Niigata", 228.9),
    ("Niigata", "Toyama", 254.1),
    ("Niigata", "Nagano", 211.3),
    ("Kofu", "Nagano", 164),
    ("Toyama", "Kanazawa", 59.4),
    ("Toyama", "Nagano", 192.8),
    ("Nagano", "Nagoya", 250.8),
    ("Kofu", "Nagoya", 262.8),
    ("Shizuoka", "Nagoya", 185.8),
    ("Kanazawa", "Fukui", 76.7),
    ("Fukui", "Kyoto", 148.1),
    ("Gifu", "Nagoya", 30.3),
    ("Gifu", "Otsu", 107.3),
    ("Nagoya", "Tsu", 66.5),
    ("Tsu", "Otsu", 84.4),
    ("Tsu", "Wakayama", 365.4),
    ("Tsu", "Nara", 89.5),
    ("Otsu", "Kyoto", 10),
    ("Kyoto", "Nara", 41.7),
    ("Osaka", "Nara", 52),
    ("Kyoto", "Osaka", 39),
    ("Kyoto", "Tottori", 253.5),
    ("Kyoto", "Kobe", 77.4),
    ("Osaka", "Kobe", 36.9),
    ("Osaka", "Wakayama", 76.1),
    ("Kobe", "Okayama", 143.4),
    ("Tokushima", "Takamatsu", 74.5),
    ("Okayama", "Takamatsu", 71.8),
    ("Wakayama", "Tokushima", 65.8),
    ("Tokushima", "Kochi", 156.7),
    ("Takamatsu", "Kochi", 159.3),
    ("Tottori", "Okayama", 141.8),
    ("Takamatsu", "Matsuyama", 194.4),
    ("Okayama", "Hiroshima", 161.3),
    ("Tottori", "Matsue", 121.6),
    ("Matsuyama", "Kochi", 251.2),
    ("Matsue", "Yamaguchi", 256.5),
    ("Hiroshima", "Yamaguchi", 132.8),
    ("Hiroshima", "Matsuyama", 66.2),
    ("Matsuyama", "Oita", 166.5),
    ("Yamaguchi", "Hakata", 147.9),
    ("Hakata", "Oita", 198.5),
    ("Hakata", "Saga", 53.6),
    ("Hakata", "Kumamoto", 118.4),
    ("Kumamoto", "Oita", 148),
    ("Oita", "Miyazaki", 207),
    ("Saga", "Nagasaki", 100.3),
    ("Kumamoto", "Kagoshima", 170.5),
    ("Miyazaki", "Kagoshima", 125.9),
    ("Nagasaki", "Naha", 758),
    ("Kagoshima", "Naha", 673.7)
]

for edge in edges:
    g.addEdge(edge[0], edge[1], edge[2])


max_hops = 6
avg_distances = g.find_avg_distances_for_hops(max_hops)

for node, distances in avg_distances.items():
    print(f"Node: {node}")
    for path_info, avg_distance in distances.items():
        print(f"{path_info}: {avg_distance}")

# max_hops = 6
# avg_distances = []
# for node in g.graph:
#     for target in g.graph:
#         if node != target:
#             paths = g.findPaths(node, target, max_hops)
#             distances = g.findPathDistances(paths)
#             if distances:
#                 avg_distance = sum(distances) / len(distances)
#                 avg_distances.append(avg_distance)
#
# print("Average distance for all paths with up to {} hops: {}".format(max_hops, sum(avg_distances) / len(avg_distances)))


