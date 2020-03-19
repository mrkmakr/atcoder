class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        
        if self.parent[a] == self.parent[b]:
            return
        if self.size[a] >= self.size[b]:
            self.parent[b] = a
            self.size[a] += self.size[b]
        else:
            self.parent[a] = b
            self.size[b] += self.size[a]
        
    def is_same(self, a, b):
        return self.find(a) == self.find(b)
    
    def count(self, x):        
        return self.size[self.find(x)]
