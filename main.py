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
            print("")

            # Reset Graph to original State
            if userInput == "1":
                G, pos, color_map = generateGraph(10, 1)
                print("\nGraph reset!")

            # Remove Random Node
            elif userInput == "2":
                rand_removal_of_node(G, color_map=color_map)

            # Remove Selected Node
            elif userInput == "3":
                kill_node(G, color_map=color_map)

            # Display Graph
            elif userInput == "4":
                displayGraph(G, pos, color_map=color_map)

            # Calculate Shortest Path
            elif userInput == "5":                
                src = input("Source Node: ")
                dest = input("Destination Node: ")
                prev_nodes, shortest_paths = dijkstra_algorithm(G, src)

                try:               
                    cur_node = int(dest)
                    optimal_path = []
                    while True:
                        optimal_path.insert(0, cur_node)
                        if cur_node == int(src):
                            break
                        cur_node = prev_nodes[cur_node]
                        
                    print(f'Optimal Path from Node {src} to Node {dest}: {optimal_path}')
                    print(f'Optimal Path Cost from Node {src} to Node {dest}: {round(shortest_paths[int(dest)], 2)}')
                    path_edges = list(zip(optimal_path,optimal_path[1:]))

                    displayGraph(G, pos, color_map=color_map, path_edges=path_edges)

                except:
                    print("\nPath not possible")

                # djikstra(G, 7, 5, pos)

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
3 - Remove Selected Node
4 - Show Graph
5 - Calculate Shortest Path
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

def kill_node(graph, color_map):
    hasAliveNodes = False
    valid_nodes = []
    for node in graph.nodes:
        num_neighbors = graph.neighbors(node)
        if len(list(num_neighbors)) != 0:
            valid_nodes.append(node)
            hasAliveNodes = True

    if hasAliveNodes:
        x = input("choose a node to kill: ")

        if int(x) not in valid_nodes:
            print(f'Node {x} is already dead!')
            return

        rm_edges = list(graph.edges(int(x)))
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

def dijkstra_algorithm(graph, start_node):

    output_path = []
    unvisited_nodes = list(graph.nodes())
    shortest_path = {}
    previous_nodes = {}
 
    
    max_value = 10
    for node in unvisited_nodes:
        shortest_path[node] = max_value
   
    shortest_path[int(start_node)] = 0
    
   
    while unvisited_nodes:
        
        current_min_node = None
        
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        
        neighbors = list(graph.neighbors(current_min_node))
        
        for neighbor in neighbors:
           
            tentative_value = shortest_path[current_min_node] + graph[current_min_node][neighbor]["weight"]
            
            if tentative_value < shortest_path[neighbor]:
               
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
                output_path.append(neighbor)
                
        unvisited_nodes.remove(current_min_node)

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