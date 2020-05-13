"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Starting off the set with the first vertex_id
        self.vertices[vertex_id] = set()
        
        pass  

    def add_edge(self, v1, v2):
        # This is to check if the vertices are in the graph
		if v1 in self.vertices and v2 in self.vertices:
            # this adds vertex 2 on vertex 1's set of edges.
            self.vertices[v1].add(v2)
​     
    # or else return this:
		else:
			raise IndexError("Vertex does not exist in graph")
        
        pass  

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    
        pass  

    def bft(self, starting_vertex):

        # create a queue class
		q = Queue()
        # enqueue is adding onto the list, so we being at starting_vertex_id
		q.enqueue(starting_vertex)
​
		# we need to create a set that Keeps track of visited nodes
		visited = set()
​
		# Repeat if there is still things in the queue until queue is empty
		while q.size() > 0:
			
			# Dequeue is removing from the list - we do that to first vertices
			v = q.dequeue()
​
			# If it's not visited, check the set above:
			if v not in visited:
				print(v)
​
				# Mark visited if it is in the visited set
				visited.add(v)
​
                # this is the next step after dequeuing
                # we then check the adjacent neighbours 
				for next_vert in self.get_neighbors(v):
                    # we then add it onto the queue
					q.enqueue(next_vert)
     
        pass  

    def dft(self, starting_vertex):

        # create a stack class
		s = Stack()
        # push is adding onto the list, so we being at starting_vertex_id
		s.push(starting_vertex)
​
		# we need to create a set that Keeps track of visited nodes
		visited = set()
​
		# Repeat if there is still things in the queue until queue is empty
		while s.size() > 0:
			
			# Pop is removing from the list - we do that to first vertices
			v = s.pop()
​
			# If it's not visited, check the set above:
			if v not in visited:
				print(v)
​
				# Mark visited if it is in the visited set
				visited.add(v)
​
                # this is the next step after dequeuing
                # we then check the adjacent neighbours 
				for next_vert in self.get_neighbors(v):
                    # we then add it onto the queue
					s.push(next_vert)


        pass  

    # Do with recursion
    def dft_recursive(self, starting_vertex, visited=None):
        # Check if visisted is None
        if visited is None:
            # If it id none, change it to a set
            visited = set()

        print(starting_vertex)

        # start of with the first vertex
        visited.add(starting_vertex)

        # check for neighbouring nodes
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
      
        pass  
        
    # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.
    def bfs(self, starting_vertex, destination_vertex):

        # create a queue class
		q = Queue()
        # enqueue is adding onto the list, so we being at starting_vertex_id
		q.enqueue(starting_vertex)
​
		# we need to create a set that Keeps track of visited nodes
		visited = set()
​
		# Repeat if there is still things in the queue until queue is empty
		while q.size() > 0:
			
			# Here we create a path
            # Dequeue is removing from the list - we do that to first vertices
			path = q.dequeue()
​            
            # Get the last vertex from the PATH
            last_vertex = path[-1]

			# If last_vertex not visited, check the neighbours:
			if last_vertex not in visited:
                # if the last_vertex is the destination, return the path
                if last_vertex == destination_vertex:
                    return path
                # else, we create new paths with each neighbour
                else:
                    for next_vert in self.get_neighbors(last_vertex):
                        # Then we add it onto the queue
                        q.enqueue(path + next_vert)
			​
				# Mark visited if it is in the visited set
				visited.add(last_vertex)
​
            

        
        pass  

    # Return a list containing a path from starting_vertex to destination_vertex in depth-first order.
    def dfs(self, starting_vertex, destination_vertex):
        
        # create a stack class
		s = Stack()
        # push is adding onto the list, so we being at starting_vertex_id
		s.push(starting_vertex)
​
		# we need to create a set that Keeps track of visited nodes
		visited = set()
​
		# Repeat if there is still things in the queue until queue is empty
		while s.size() > 0:
			
			# Here we create a path
            # Pop is removing from the list - we do that to first vertices
			path = s.pop()
​
			# Get the last vertex from the PATH
            last_vertex = path[-1]

			# If last_vertex not visited, check the neighbours:
			if last_vertex not in visited:
                # if the last_vertex is the destination, return the path
                if last_vertex == destination_vertex:
                    return path
                # else, we create new paths with each neighbour
                else:
                    for next_vert in self.get_neighbors(last_vertex):
                        # Then we add it onto the queue
                        s.push(path + next_vert)
			​
				# Mark visited if it is in the visited set
				visited.add(last_vertex)


        pass  

    # Return a list containing a path from starting_vertex to destination_vertex in depth-first order.
    def dfs_recursive(self, starting_vertex, destination_vertex):
        # Check if visisted is None
        if visited is None:
            # If it id none, change it to a set
            visited = set()

        if path is None:
            path = []
        
        # start of with the first vertex
        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        
        # check for neighbouring nodes
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                new path = self.dft_recursive(next_vert, visited, destination_vertex, path)
        
  
        pass  

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
