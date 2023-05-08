# CPE400 Final Project

Colin Martires, Davis Dunkley, Dustin Mader

5/2/2023

Topic 4: Dynamic routing echanism design in faulty network

## Requirements

* python 
* pyvis
* networkx

**To Run Program**

Please make sure that the right packages are installed, to do so enter the following code into the terminal.

* `pip install -r requirements.txt`

After the required packages have been installed.

To run the program you will input the code into terminal: 

* `python main.py`

This will start the program where you the user will be propmted to enter a command. (1 - 6)
Each command will have a utility that has its unique functionailty. 

1 - reset graph 
  - will restore the nodes if any have been deleted or made inactive 

2 - Remove Random Node
  - will chose a random node and deactivate it from the map 

3 - Remove Selected Node
  - will allow the user to choose which node they want to deactivate.

4 - Show Graph 
  - Is the display functionaily it will display the graph with the current status of each node if active or deactive

5 - Calcuate Shortest Path 
  - This will display the path of to the nodes after asking the user which nodes they want a path too if there is a path it will display it and also calcuate the optimal weight.
  - If there is no path a message will display propmting to the user that the path could not be made. 

6 - Exit
  - will exit the program.
