from collections import defaultdict 
#agar  tidak menggunakan argumen dan memberikan nilai default untuk kunci yang tidak ada.
class Graph:   
    def __init__(self,vertices): 
        self.V = vertices 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def DLS(self,src,target,maxDepth): 
        if src == target : return True
        if maxDepth <= 0 : return False
        for i in self.graph[src]:
            print("Posisi :", i)
            if(self.DLS(i,target,maxDepth-1)): 
                return True
        return False

    def IDDFS(self,src, target, maxDepth):                 
        for i in range(maxDepth):                                  
            print("Level :", i)
            print("Posisi :", src)
            if (self.DLS(src, target, i)):  
                return True
            print()
        return False
   
g = Graph(7); 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 
  
target = 6; maxDepth = 3; src = 0
  
print(g.IDDFS(src, target, maxDepth))
