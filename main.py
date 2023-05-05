# Authors: Davis Dunkley, Colin Martires, Dustin Mader
# 5/4/2023
# CPE400  Computer Communication Networks
# Final Project - Topic 4 Dynamic routing mechanism design in faulty network

import matplotlib.pyplot as plt
import networkx as nx
import random as rnd
import math as math

def main():
    G, pos = generateGraph(10)

    rand_removal_of_node(G)

    djikstra(G, pos, 1, 8)

    
def rand_removal_of_node(graph):
    fail_number = round(rnd.random(), 2)
    print(list(graph.nodes(data=True)))

    for n in range(0,graph.number_of_nodes()):
        print(graph[n])
        if graph[n]["weight"] <= fail_number:
             graph.remove_node(n)
             print("removed node: " , n)
             break
            
    # print(list(graph.nodes(data=True)))
    # x = rnd.randint(1, graph.number_of_nodes())
    # print("removed node: " , x)
    # graph.remove_node(x)
    

def djikstra(graph, pos, begin, end):

    # change to own djikstra implementation
    path = nx.shortest_path(graph,source=begin,target=end)
    
    
    path_edges = list(zip(path,path[1:]))
    nx.draw_networkx_nodes(graph, pos, node_size=700)
    nx.draw_networkx_edges(graph,pos,edge_color='b',width=1)
    nx.draw_networkx_edges(graph,pos,edgelist=path_edges,edge_color='r',width=5)
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    total_weight = 0
    for e in path_edges:
        print((graph[e[0]][e[1]]["weight"]))
        total_weight += (graph[e[0]][e[1]]["weight"])
    
    print(f'Optimal Path: {path}')
    print(f'Optimal Path Weight: {round(total_weight, 2)}')
    


def generateGraph(n):
    G = nx.random_internet_as_graph(n, 1234)

    for e in G.edges():
        G[e[0]][e[1]]["weight"] = round(rnd.random(), 2)

    for i in range(0, G.number_of_nodes()):
        G.nodes[i]["prob_of_failure"] = round(rnd.random(), 2)


    pos = nx.spring_layout(G, seed=2)  # positions for all nodes - seed for reproducibility
    nx.draw(G,pos,node_color='k')

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=500)

    # nx.draw_networkx_edges(G, pos, width=6)


    # edges
    # nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    # nx.draw_networkx_edges(
    #     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    # )

    # nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
    # nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=5)

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
    # # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    return G, pos




if __name__ == "__main__":
    main()