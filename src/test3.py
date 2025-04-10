import itertools
import networkx as nx
from Distcal import *

hops = 1
i =1
for i in range (6):
    print("Average distance for", hops, "hops:", calc_average_distance(hops))
    hops += 1


