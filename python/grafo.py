import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


df_edges = pd.read_csv('./Edges_GOT.csv')
df_nodes = pd.read_csv('./Nodes_GOT.csv')


G = nx.Graph()
G = nx.from_pandas_edgelist(df_edges, 'Source', 'Target', ['type','color','lty'], create_using=nx.Graph())
G.add_nodes_from(df_nodes['Id'])


def farness_centrality(G):
    farness_centrality = {}
    for node in G.nodes:
        length=nx.single_source_shortest_path_length(G, node)
        farness_centrality[node] = sum(length.values())

    return farness_centrality


print("_______________________________________________________________________")
print("centralidad del grafo")
centralidad = nx.degree_centrality(G)
print(centralidad)

##intermediacion
print("_________________________________________________________________________")
print("intermediacion")
intermediacion = nx.betweenness_centrality(G)
print(intermediacion)


##cercania
print("_________________________________________________________________________")
print("cercania")
cercania = nx.closeness_centrality(G)
print(cercania)

print("_________________________________________________________________________")
print("matriz de adyacencia")
matriz = nx.adjacency_matrix(G)
print(matriz.todense())


nx.draw(G)
plt.show()

