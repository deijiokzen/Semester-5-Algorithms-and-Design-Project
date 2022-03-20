from main import *


class BellmanGraph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def list_edge_add(self, list):
        for i in range(len(list)):
            for j in range(len(list)):
                if list[i][j] != INT_MAX:
                    self.addEdge(i, j, list[i][j])

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        str1=""
        #print("Vertex Distance from Source")
        str1+="Vertex Distance from Source\n"
        for i in range(self.V):
            str1+=str(i) + "\t\t" + str(dist[i]) +"\n"
            #print("{0}\t\t{1}".format(i, dist[i]))
        print(str1)
        return str1;

    def BellmanFord(self, src):


        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w



        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        return self.printArr(dist)

#GlobalData=getglobaldata("input10.txt")
#g = BellmanGraph(GlobalData[0])
#g.list_edge_add(GlobalData[3])
#x=g.BellmanFord(GlobalData[1])
#print(x)