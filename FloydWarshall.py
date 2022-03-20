from main import *
# Number of vertices



# Algorithm
def floyd(G,nV):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    return sol(dist,nV)

# Printing the output
def sol(dist,nV):
    str1=""
   # matrix=[[]]
   # matrix= np.zeros((nV, nV))
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INT_MAX):
                str1+="INF\t\t"
                #print("INF", end="\t\t")
            else:
                str1+=str(round(dist[p][q],1))
                str1+="\t\t"
                #print(round(dist[p][q],1), end="\t\t")
        str1+="\n"

    return str1




#GlobalData=getglobaldata("input10.txt")
#print(GlobalData[3])
#floyd(GlobalData[3],GlobalData[0])

#floyd(G,10)