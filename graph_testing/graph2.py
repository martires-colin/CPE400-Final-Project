import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge("a", "b", weight=0.6)
G.add_edge("a", "c", weight=0.2)
G.add_edge("c", "d", weight=0.1)
G.add_edge("c", "e", weight=0.7)
G.add_edge("c", "f", weight=0.9)
G.add_edge("a", "d", weight=0.3)
G.add_edge("f", "g", weight=0.5)
G.add_edge("f", "h", weight=0.5)
G.add_edge("c", "h", weight=0.5)
G.add_edge("d", "i", weight=0.3)
G.add_edge("d", "h", weight=0.9)
G.add_edge("a", "e", weight=0.9)

# Maybe use this to color shortest path
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

# ---get shortest path
path = nx.shortest_path(G,source="g",target="d")
path_edges = list(zip(path,path[1:]))




pos = nx.spring_layout(G, seed=2)  # positions for all nodes - seed for reproducibility
nx.draw(G,pos,node_color='k')

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
# nx.draw_networkx_edges(
#     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
# )

nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=5)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()