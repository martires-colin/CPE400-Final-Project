from pyvis.network import Network
import networkx as nx

# Different Graph Configurations
# nx_graph = nx.random_lobster(3, 0.60, 0.90)
# nx_graph = nx.karate_club_graph()
# nx_graph = nx.davis_southern_women_graph()
# nx_graph = nx.florentine_families_graph()
# nx_graph = nx.les_miserables_graph()
nx_graph = nx.random_internet_as_graph(20)

for i in range(0, len(nx_graph.nodes)):
    nx_graph.nodes[i]['title'] = str(i)
    nx_graph.nodes[i]['label'] = str(i)



nt = Network()

nt.from_nx(nx_graph)

nt.show("networkx.html", local=True, notebook=False)