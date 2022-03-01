from cmath import inf
import networkx as nx
import numpy
import matplotlib.pyplot as plt

configs = [(1000, 0.1), (3000, 0.01), (5000, 0.02)]



for i in configs:
    avg_cluster = []
    avg_pathlen = []
    avg_deg = []
    for _ in range(5):
        G = nx.erdos_renyi_graph(i[0],i[1])
        avg_cluster.append(nx.average_clustering(G))
        if nx.is_connected(G):
            avg_pathlen.append(nx.average_shortest_path_length(G))
        deg = [val for node,val in G.degree()]
        avg_deg.append(numpy.mean(deg))
    
    
    print("for configuration", i, "average clutering is:", numpy.mean(avg_cluster) )
    print("for configuration", i, "average path length is:", numpy.mean(avg_pathlen))
    print("for configuration", i, "average degree is:", numpy.mean(avg_deg))
    plt.hist(deg)

# plt.xlabel("iterations")
plt.ylabel("degree distribution")
plt.legend(["config 1", "config 2", "config 3"])
plt.show()

        
