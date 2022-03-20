from main import *


class KruskalGraph:
    def __init__(self, vertex):
        self.edges = list(G.edges.keys())
        G.remove_edges_from(self.edges)
        self.V = vertex
        self.graph = []


    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def list_edge_add(self, list):
        for i in range(len(list)):
            for j in range(len(list)):
                if list[i][j] != INT_MAX:
                    self.add_edge(i, j, list[i][j])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        self.sum=0
        for u, v, weight in result:
            print("Edge:", u, v, end=" ")
            G.add_edge(u,v)
            print("-", weight)
            self.sum+=weight
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown')
        # plt.show()

        # Get Old Graph Back
        return [self.sum,self.edges]

#g= KruskalGraph(x)

#g.list_edge_add(directed)
#g.kruskal()
