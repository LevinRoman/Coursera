import unittest

class WeightedGraph(dict):
    def __init__(self):
        super().__init__(self)
        self._totalLengthUpperBound = 1
        
    def AddVertex(self, vertex):
        if vertex not in self:
            self[vertex] = dict()
            
    def AddEdge(self, vertex1, vertex2, length):
        if length > 0:
            self.AddVertex(vertex1)
            self.AddVertex(vertex2)
            if vertex2 not in self[vertex1]:
                self[vertex1][vertex2] = length
                self[vertex2][vertex1] = length
                self._totalLengthUpperBound += length
            
    def HasVertex(self, vertex):
        return vertex in self
    
    def HasEdge(self, vertex1, vertex2):
        return self.HasVertex(vertex1) and (vertex2 in self[vertex1])
    
    def EdgeLength(self, vertex1, vertex2):
        if self.HasVertex(vertex1):
            return self[vertex1].get(vertex2)

    #generator for all vertices of the graph
    def Vertices(self):
        return self.keys()

    #generator for all adjacent vertices of the given vertex
    def AdjacentVertices(self, vertex):
        if self.HasVertex(vertex):
            return self[vertex].keys()
        
    @property
    def totalLengthUpperBound(self):
        return self._totalLengthUpperBound
    


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

class TestSpanningTree(unittest.TestCase):
    
    def setUp(self):
        self.graph = WeightedGraph()
        self.graph.AddEdge(1,2,4) 
        self.graph.AddEdge(2,3,7) 
        self.graph.AddEdge(3,4,5) 
        self.graph.AddEdge(2,5,10) 
        self.graph.AddEdge(5,6,11) 
        self.graph.AddEdge(5,3,13) 
        self.graph.AddEdge(2,4,9) 


    def test_number_of_vertices(self):
        self.assertEqual(len(list(self.graph.Vertices())), len(list(GetMinimumSpanningTree(self.graph).Vertices())))

    def test_number_of_edges(self):
        k = 0
        for i in GetMinimumSpanningTree(self.graph).Vertices():
            k = k + len(list(GetMinimumSpanningTree(self.graph).AdjacentVertices(i)))
        k = k/2
        self.assertEqual(k, len(list(self.graph.Vertices())) - 1)

    def test_example_one(self):
        self.assertEqual(GetMinimumSpanningTree(self.graph), {1: {2: 4}, 2: {1: 4, 3: 7, 5: 10}, 3: {2: 7, 4: 5}, 4: {3: 5}, 5: {2: 10, 6: 11}, 6: {5: 11}})

    def test_example_two(self):
        self.graph = WeightedGraph()
        self.graph.AddEdge(1,2,1)
        self.assertEqual(GetMinimumSpanningTree(self.graph), {1: {2: 1}, 2: {1: 1}})
        
    def test_weight_bound(self):
        self.graph = WeightedGraph()
        self.graph.AddEdge(1,2,8)
        self.graph.AddEdge(1,3,2)
        self.graph.AddEdge(1,4,8)
        self.graph.AddEdge(1,5,3)
        self.graph.AddEdge(1,6,2)
        self.graph.AddEdge(2,3,3)
        self.graph.AddEdge(2,4,3)
        self.graph.AddEdge(2,5,9)
        self.graph.AddEdge(2,6,2)
        self.graph.AddEdge(3,4,2)
        self.graph.AddEdge(3,5,3)
        self.graph.AddEdge(3,6,7)
        self.graph.AddEdge(4,5,9)
        self.graph.AddEdge(4,6,2)
        self.graph.AddEdge(5,6,2)
        k = 0
        for i in GetMinimumSpanningTree(self.graph).Vertices():
            for j in GetMinimumSpanningTree(self.graph)[i].values():
                k = k + j
        k = k/2
        self.assertTrue(k < 65)

    def test_weight_equal(self):
        self.graph = WeightedGraph()
        self.graph.AddEdge(1,2,2)
        self.graph.AddEdge(1,3,2)
        self.graph.AddEdge(1,4,2)
        self.graph.AddEdge(1,5,2)
        self.graph.AddEdge(1,6,2)
        self.graph.AddEdge(2,3,2)
        self.graph.AddEdge(2,4,2)
        self.graph.AddEdge(2,5,2)
        self.graph.AddEdge(2,6,2)
        self.graph.AddEdge(3,4,2)
        self.graph.AddEdge(3,5,2)
        self.graph.AddEdge(3,6,2)
        self.graph.AddEdge(4,5,2)
        self.graph.AddEdge(4,6,2)
        self.graph.AddEdge(5,6,2)
        k = 0
        for i in GetMinimumSpanningTree(self.graph).Vertices():
            for j in GetMinimumSpanningTree(self.graph)[i].values():
                k = k + j
        k = k/2
        self.assertEqual(k, 2*(6-1))
        
    def test_example_three_palka(self):
        self.graph = WeightedGraph()
        self.graph.AddEdge(1,2,1)
        self.graph.AddEdge(2,3,2)
        self.graph.AddEdge(3,4,3)
        self.graph.AddEdge(4,5,4)
        self.assertEqual(GetMinimumSpanningTree(self.graph), self.graph)
        
    def test_example_star(self):
        self.graph = WeightedGraph() 
        self.graph.AddEdge(1,2,1) 
        self.graph.AddEdge(1,3,3) 
        self.graph.AddEdge(1,4,2) 
        self.graph.AddEdge(1,5,4) 
        self.graph.AddEdge(1,6,5) 
        self.graph.AddEdge(1,7,9)
        self.assertEqual(GetMinimumSpanningTree(self.graph), self.graph)
        
suite =  unittest.TestLoader().loadTestsFromTestCase(TestSpanningTree)

unittest.TextTestRunner().run(suite)
