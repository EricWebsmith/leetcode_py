# Disjoint Set Union-find algorithm

class DSU:    
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x!=self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def merge(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1
        
        self.p[px] = py
        self.e += 1
        return 0