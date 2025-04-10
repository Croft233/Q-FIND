import itertools
import networkx as nx

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

G = nx.Graph()
G.add_weighted_edges_from(edges)

def calc_average_distance(hops):
    pairs = [p for p in nx.all_pairs_shortest_path(G, cutoff=hops) if len(p[1]) > 1]

    all_pairs_distances = []
    for node, paths in pairs:
        for path in paths.values():
            if len(path) == hops + 1:  # number of hops + 1 equals number of nodes in the path
                pair_distance = sum(G[path[i-1]][path[i]]['weight'] for i in range(1, len(path)))
                all_pairs_distances.append(pair_distance)

    average_distance = sum(all_pairs_distances) / len(all_pairs_distances)
    return average_distance

