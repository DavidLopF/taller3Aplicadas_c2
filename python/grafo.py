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


degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
farness_centralityVar = farness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality_numpy(G)
katz_centrality = nx.katz_centrality(G)






degree_centrality.to_Exel('degree_centrality.xlsx')
betweenness_centrality.to_Exel('betweenness_centrality.xlsx')
closeness_centrality.to_Exel('closeness_centrality.xlsx')
farness_centralityVar.to_Exel('farness_centralityVar.xlsx')
eigenvector_centrality.to_Exel('eigenvector_centrality.xlsx')
katz_centrality.to_Exel('katz_centrality.xlsx')






nx.draw(G)
plt.show()

