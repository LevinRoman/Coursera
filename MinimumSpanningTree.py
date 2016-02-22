from ClassWeightedGraph import *
def GetMinimumSpanningTree(graph):
    spanningTree = WeightedGraph()
    V = list(graph.Vertices())
    spanningTree.AddVertex(V[0])
    min_dist = [[2**30, -1]]*len(V)
    def Change_dist(ad_vert):
        for index in range(len(V)):
            if graph.HasEdge(V[index], ad_vert):
                if graph.EdgeLength(V[index], ad_vert) < min_dist[index][0]:
                    min_dist[index] = [graph.EdgeLength(V[index], ad_vert), ad_vert]
        return min_dist
    min_dist = Change_dist(V[0])
    while len(list(spanningTree.Vertices())) < len(list(graph.Vertices())):
        minim = [2**30, -1]
        for kindex in range(len(min_dist)):
            if V[kindex] not in spanningTree.Vertices() and min_dist[kindex][0] < minim[0]:
                minim = [min_dist[kindex][0], kindex]
        spanningTree.AddEdge(min_dist[minim[1]][1], V[minim[1]], minim[0])    
        min_dist = Change_dist(V[minim[1]])    
    return spanningTree