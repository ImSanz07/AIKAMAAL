from collections import deque

class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False

class Graph:
  def __init__(self):
    self.rootNode = None

  def bfs(self):
    """
    Performs Breadth-First Search traversal on the graph.
    """
    queue = deque([self.rootNode])
    self.rootNode.visited = True
    print(f"Node: {self.rootNode.data}")

    while queue:
      current_node = queue.popleft()
      unvisited_child = self.get_unvisited_child_node(current_node)
      while unvisited_child:
        unvisited_child.visited = True
        print(f"Node: {unvisited_child.data}")
        queue.append(unvisited_child)
        unvisited_child = self.get_unvisited_child_node(current_node)

  def get_unvisited_child_node(self, node):
    """
    Replace this function with your logic to find unvisited child nodes
    specific to your graph representation.
    """
    # Replace with your implementation to find unvisited child nodes of the node
    pass

  def clear_nodes(self):
    """
    Clears the visited flag of all nodes in the graph.
    """
    for node in self.get_all_nodes():
      node.visited = False

  def get_all_nodes(self):
    """
    Replace this function with your logic to return all nodes in the graph
    specific to your graph representation.
    """
    # Replace with your implementation to return all nodes in the graph
    pass

# Example usage (assuming you have a Graph object with a populated root node)
graph = Graph()
graph.bfs()
graph.clear_nodes()  # Optional: Clear visited flags for future BFS runs


def hanoi(n, source, auxiliary, destination):
  """
  Solves the Towers of Hanoi problem using recursion.
  """
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return
  hanoi(n-1, source, destination, auxiliary)
  print(f"Move disk {n} from {source} to {destination}")
  hanoi(n-1, auxiliary, source, destination)

# Example usage
hanoi(3, 'A', 'B', 'C')
