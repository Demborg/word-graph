from itertools import groupby, combinations

import matplotlib.pyplot as plt
import networkx as nx

def main():
    words = open("words.txt").read().split()
    G = nx.Graph()
    for order in ((0, 1), (0, 2), (1, 2)):
        fun = lambda x: x[order[0]] + x[order[1]]
        grouped = groupby(sorted(words, key=fun), key=fun)
        for _, group in grouped:
            G.add_edges_from(edge for edge in combinations(group, 2))
    longest = 0
    start = ""
    end = ""
    for word1, stuff in nx.shortest_path_length(G):
        for word2, distance in stuff.items():
            if distance > longest:
                longest = distance
                start = word1
                end = word2


    print(start, "-->", end, longest)
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
