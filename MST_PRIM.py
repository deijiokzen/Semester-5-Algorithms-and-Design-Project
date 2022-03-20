from main import *







class PrimmGraph:
    def __init__(self,adjacencymatrix, totalnodes):
        self.edges = list(G.edges.keys())
        G.remove_edges_from(self.edges)

        self.cost=adjacencymatrix
        self.Max_Nodes=totalnodes


    def isValidEdge(self,u, v, inMST):
        if u == v:
          return False
        if inMST[u] == False and inMST[v] == False:
            return False
        elif inMST[u] == True and inMST[v] == True:
            return False
        return True


    def primMST(self):
        inMST = [False] * self.Max_Nodes

        # Include first vertex in MST
        inMST[0] = True

        # Keep adding edges while number of included
        # edges does not become V-1.
        edge_count = 0
        mincost = 0
        while edge_count < self.Max_Nodes - 1:

            # Find minimum weight valid edge.
            minn = INT_MAX
            a = -1
            b = -1
            for i in range(self.Max_Nodes):
                for j in range(self.Max_Nodes):
                    if self.cost[i][j] < minn:
                        if self.isValidEdge(i, j, inMST):
                            minn = self.cost[i][j]
                            a = i
                            b = j

            if a != -1 and b != -1:
                print("Edge %d: (%d, %d) cost: %f" %
                  (edge_count, a, b, minn))
                G.add_edge(a,b)
                edge_count += 1
                mincost += minn
                inMST[b] = inMST[a] = True

        print("Minimum cost = %f" % mincost)
        pos = nx.get_node_attributes(G, 'pos')

        nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown')

        return [mincost,self.edges]


#if __name__ == "__main__":

    #prim=PrimmGraph(directed,x)
    #x=prim.primMST()


