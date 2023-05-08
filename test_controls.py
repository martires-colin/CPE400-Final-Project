# Authors: Davis Dunkley, Colin Martires, Dustin Mader
# 5/4/2023
# CPE400  Computer Communication Networks
# Final Project - Topic 4 Dynamic routing mechanism design in faulty network

import matplotlib.pyplot as plt
import networkx as nx
import random as rnd
import math as math
import sys

def main():

    # Generate Initial Graph
    G, pos, color_map = generateGraph(10, 1)

    try:
        # execute loop until user decides to exit program
        while(True):
            displayMenu()
            userInput = input("Enter command: ")

            # Reset Graph to original State
            if userInput == "1":
                G, pos, color_map = generateGraph(10, 1)
                print("\nGraph reset!")

            # Remove Random Node
            elif userInput == "2":
                rand_removal_of_node(G, color_map=color_map)

            # Display Graph
            elif userInput == "3":
                displayGraph(G, pos, color_map=color_map)

            # Calculate Shortest Path
            elif userInput == "4":                
                # src = input("Source Node: ")
                # dest = input("Destination Node: ")
                dijkstra_algorithm(G, 7)
                djikstra(G, 7, 5, pos)

            # Display Menu
            elif userInput == "5":
                displayMenu()
            
            # Exit Program
            elif userInput == "6":
                print("\nExiting Program")
                return 0

            # Handle Invalid Command
            else:
                print("Please enter a valid command.")

    # Handle Keyboard Interrupt
    except KeyboardInterrupt:
        print("\nExiting Program")


def displayMenu():
    print(
        '''
---------------------------
1 - Reset Graph
2 - Remove Random Node
3 - Show Graph
4 - Calculate Shortest Path
5 - Menu Options
6 - Exit
---------------------------
        '''
    )


def displayGraph(graph, pos, color_map, path_edges = []):

    # draw nodes and edges
    nx.draw_networkx_nodes(graph,pos,node_size=300, node_color=color_map)
    nx.draw_networkx_edges(graph,pos,edge_color='b',width=1, style=':')

    # color specific edges
    nx.draw_networkx_edges(graph,pos,edgelist=path_edges,edge_color='r',width=2)

    # draw labels
    nx.draw_networkx_labels(graph, pos, font_size=11, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    # create plot
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# TODO
# remove node based on some sort node attribute
def rand_removal_of_node(graph, color_map):
    # fail_number = round(rnd.random(), 2)
    # print(list(graph.nodes(data=True)))

    # for n in range(0,graph.number_of_nodes()):
    #     print(graph[n])
    #     if graph[n]["weight"] <= fail_number:
    #          graph.remove_node(n)
    #          print("removed node: " , n)
    #          break
            
    # print(list(graph.nodes(data=True)))
    # x = rnd.randint(0, graph.number_of_nodes() - 1)

    hasAliveNodes = False
    valid_nodes = []
    for node in graph.nodes:
        num_neighbors = graph.neighbors(node)
        if len(list(num_neighbors)) != 0:
            valid_nodes.append(node)
            hasAliveNodes = True

    if hasAliveNodes:
        x = rnd.choice(valid_nodes)
        rm_edges = list(graph.edges(x))
        for edge in rm_edges:
            graph.remove_edge(edge[0], edge[1])
        print("Killed node: " , x)

        # Change color of dead nodes
        for node in graph.nodes:
            num_neighbors = graph.neighbors(node)
            if len(list(num_neighbors)) == 0:
                color_map[node] = "red"
        return x
    else:
        print("All nodes are dead!")
        return


# TODO
# implement djikstra
def djikstra(graph, start_node, end, pos):
    path = nx.shortest_path(graph,source=start_node,target=end)
    
    
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
    



def dijkstra_algorithm(graph, start_node):
    # unvisited_nodes = list(graph.get_nodes())
    unvisited_nodes = list(graph.nodes())
    print(f'Unvisited Nodes: {unvisited_nodes}')

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = 10
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[int(start_node)] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        print(f'Current Min Node: {current_min_node}')
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        print(f'Current Min Node: {current_min_node}')

        # The code block below retrieves the current node's neighbors and updates their distances
        # neighbors = graph.get_outgoing_edges(current_min_node)
        neighbors = list(graph.neighbors(current_min_node))
        print(f"{current_min_node}'s neighbors {neighbors}")

        print(f'shortest paths: {shortest_path}')
        for neighbor in neighbors:
            # tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            tentative_value = shortest_path[current_min_node] + graph[current_min_node][neighbor]["weight"]
            # print(f'Node []')
            if tentative_value < shortest_path[neighbor]:
                
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
        print(f'Unvisited Nodes: {unvisited_nodes}')

    print(shortest_path)
    print(previous_nodes)
    
    return previous_nodes, shortest_path


def generateGraph(n, seed):

    # Generate Random Graph Following AS Pattern
    G = nx.random_internet_as_graph(n,seed=seed)
    color_map = []

    # Set Randomized Edge Weights
    for e in G.edges():
        G[e[0]][e[1]]["weight"] = round(rnd.random(), 2)

    # Set Probability of Failure and Color for each node
    for i in range(0, G.number_of_nodes()):
        G.nodes[i]["prob_of_failure"] = round(rnd.random(), 2)
        color_map.append("tab:blue")

    # positions for all nodes - seed for reproducibility
    pos = nx.spring_layout(G, seed=seed)

    return G, pos, color_map

if __name__ == "__main__":
    main()