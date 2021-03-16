class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # self.graph เป็นการจัดเก็บข้อมูลเส้นเชื่อมด้วย list ของเส้นเชื่อมที่มี 3 ค่า คือ u,v,w โดย u คือ source, v คือ destination, w คือ weight

    def addEdge(self, u, v, w): # เมื่อมีการเพิ่มเส้นเชื่อมจะมีการเพิ่มข้อมูลใน list
        self.graph.append([u, v, w])

# ตัวอย่างการประกาศ method ชื่อ find_set

    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

# ตัวอย่างการประกาศ method ชื่อ union

    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1

    def kruskal(self):
        answer = []
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
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                answer.append([u, v, w])
                self.union(parent, rank, x, y)
        weight = 0
        for u, v, w in answer:
            print('Edge ระหว่าง Vertex {} กับ Vertex {} มีค่า weight = {}'.format(u, v, w))
            weight += w
        print('\nWeight รวมของ Minimum spanning tree คือ {}'.format(weight))

g = Graph(int(input('โปรดระบุจุด (Vertex) ในกราฟ: ')))
for i in range(int(input('โปรดระบุจำนวนเส้นเชื่อม (Edge) ในกราฟ: '))):
    source = int(input('Source = '))
    destination = int(input('Destination = '))
    weight = int(input('Weight = '))
    g.addEdge(source, destination, weight)
g.kruskal()

# g = Graph(9)
# g.addEdge(0,1,4)
# g.addEdge(1,2,8)
# g.addEdge(2,3,7)
# g.addEdge(3,4,9)
# g.addEdge(4,5,10)
# g.addEdge(5,6,2)
# g.addEdge(6,7,1)
# g.addEdge(7,8,7)
# g.addEdge(0,7,8)
# g.addEdge(8,2,2)
# g.addEdge(2,5,4)
# g.addEdge(6,8,6)
# g.addEdge(3,5,14)
# g.addEdge(1,7,11)
# g.kruskal()