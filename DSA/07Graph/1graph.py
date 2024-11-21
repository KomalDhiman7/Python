class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for e in range(vno)] #*is repition operator

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid Vertex")

    def remove_edge(self,u,v) :
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid Vertex")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("INVALID VERTEX")

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))

graph=Graph(5)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(3,4)

graph.print_adj_matrix()