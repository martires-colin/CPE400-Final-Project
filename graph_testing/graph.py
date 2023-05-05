from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt

# Different Graph Configurations
# nx_graph = nx.random_lobster(3, 0.60, 0.90)
# nx_graph = nx.karate_club_graph()
# nx_graph = nx.davis_southern_women_graph()
# nx_graph = nx.florentine_families_graph()
# nx_graph = nx.les_miserables_graph()
nx_graph = nx.random_internet_as_graph(10, 1234)

for i in range(0, len(nx_graph.nodes)):
    nx_graph.nodes[i]['title'] = str(i)
    nx_graph.nodes[i]['label'] = str(i)

print(nx_graph.edges[(0,1)])

# for i in range(0, len(nx_graph.edges)):
#     nx_graph.edges[i]

# for edge in nx_graph.edges:
#     print(edge.data("weight"))


nt = Network()

nt.from_nx(nx_graph)

# nt.toggle_physics(False)
# nt.toggle_drag_nodes(False)

# Generate graph through pyvis
# nt.show("networkx.html", local=True, notebook=False)
nt.show("networkx2.html", local=True, notebook=False)

# Generate graph through matplotlib
# ax = plt.gca()
# ax.margins(0.08)
# plt.axis("off")
# plt.tight_layout()
# plt.show()