import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from sys import maxsize
import numpy as np
import networkx as nx
INT_MAX = maxsize


G=nx.Graph()

def returngraphtooriginal(edges):
    Temp = list(G.edges.keys())
    G.remove_edges_from(Temp)
    G.add_edges_from(edges)


global FILE_NAME,dif_x,dif_src,dif_directed,dif_undirected
FILE_NAME=""
dif_x=0
dif_src=0
dif_directed=[[]]
dif_undirected=[[]]

class FileExtract:

    def getgraphing(self,fname):


        global FILE_NAME,dif_x,dif_directed,dif_undirected,dif_src
        if(FILE_NAME!= fname):
            f = open(fname, 'r')
            for _ in range(2):
                next(f)
            x = -1000
            i = 0
            directed = [[]]
            undirected = [[]]
            for line in f.readlines():
                if (int(x) == -1000):
                    x = int(line)
                    # print(x)
                    directed = np.zeros((x, x))
                    undirected = np.zeros((x, x))
                    indices_zero = directed == 0
                    indices_zero1 = undirected == 0
                    undirected[indices_zero1] = INT_MAX
                    directed[indices_zero] = INT_MAX
                    # print(k)


                elif (int(i) < int(x)):
                    line = line.replace('\n', '')
                    if line != '':
                        fields = line.split('\t')
                        # print(i)
                        # print(fields)
                        G.add_node(int(fields[0]), pos=(float(fields[1]), float(fields[2])))
                        i += 1


                elif (int(i) >= int(x)):
                    line = line.replace('\n', '')
                    if line != '':
                        fields1 = line.split('\t')

                        if len(fields1) != 1:
                            fields1.pop()
                            # print(fields1)
                            z = int(fields1[0])

                            j = 1
                            while (j < len(fields1)):

                                if (j != 0):
                                    # print(z, int(float(fields1[j])), int(float(fields1[j + 2])))
                                    if z != int(fields1[j]):
                                        directed[z][int(fields1[j])] = float(fields1[j + 2]) / 10 ** 7
                                        G.add_edge(z, int(fields1[j]))
                                        if directed[int(fields1[j])][z] == 0:
                                            directed[int(fields1[j])][z] = float(fields1[j + 2]) / 10 ** 7

                                    if undirected[z][int(fields1[j])] > float(fields1[j + 2]) / 10 ** 7 and z != int(fields1[j]):
                                        undirected[z][int(fields1[j])] = float(fields1[j + 2]) / 10 ** 7
                                        undirected[int(fields1[j])][z] = float(fields1[j + 2]) / 10 ** 7

                                    j += 4
                        else:

                            b = int(fields1[0])
            f.close()

            pos = nx.get_node_attributes(G, 'pos')

            nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown')
            FILE_NAME=fname
            dif_x = x
            dif_directed = directed
            dif_undirected = undirected
            dif_src = b
            return [x, b, directed, undirected]
        else:

            return [dif_x, dif_src, dif_directed, dif_undirected]



#F1=FileExtract("input10.txt")
#GlobalData = None



def getglobaldata(filename):
    F1 = FileExtract()
    GlobalData = F1.getgraphing(filename)
    #undirected=GlobalData[3]
   # indices_zero1 = undirected == INT_MAX
    #undirected[indices_zero1] = 0
    #print(undirected)
    return GlobalData

#getglobaldata("input10.txt")
#print (directed)
#indices_zero = undirected == INT_MAX
#undirected[indices_zero] = 0
#print(undirected)
#pos = nx.get_node_attributes(G, 'pos')
#nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown')
#plt.show()


