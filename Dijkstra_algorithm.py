class AdaptedHeap:
    def __init__(self):
        self.A=[]

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def insert(self, key):
        self.A.append(key)
        idx = self.__len__()-1
        self.heapify_up(idx)


    def heapify_up(self, k):
        while k>0 and self.A[(k-1)//2] >= self.A[k]:
            self.A[k],self.A[(k-1)//2] = self.A[(k-1)//2],self.A[k]
            k = (k-1)//2


    def heapify_down(self, k):
        while 2*k+1<self.__len__():
            L,R = 2*k+1,2*k+2
            m = k
            if self.A[k]>self.A[L]:
                m = L
            if R<self.__len__() and self.A[R]<self.A[m]:
                m = R
            if m!=k:
                self.A[k],self.A[m] = self.A[m],self.A[k]
                k = m
            else:
                break
    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            self.A.pop()

    def find_min(self):
        if self.__len__() == 0:
            return None
        else:
            return self.A[0]
        #빈 heap이면 None 리턴, 아니면 min값 리턴

    def delete_min(self):
        if self.__len__() == 0:
            return None
        else:
            if self.__len__() == 1:
                return self.A.pop()
            else:
                self.A[0], self.A[self.__len__() - 1] = self.A[self.__len__() - 1], self.A[0]
                min = self.A.pop()
                for i in range(self.__len__() - 1, -1, -1):
                    self.heapify_down(i)
        return min
        # 빈 heap이면 None리턴, 아니면 min 값 지운 후 리턴

    def update_key(self, old_key, new_key):
        if old_key not in self.A:
            return None
        else:
            if self.A[0] == old_key:
                self.A[0] = new_key
                self.heapify_down(0)
            else:
                a = self.A.index(old_key)
                self.A[a] = new_key
                if new_key < self.A[(a-1)//2]:
                    self.heapify_up(a)
                else:
                    self.heapify_down(a)
        #old_key가 힙에 없으면 None 리턴
        #아니면, new_key값이 최종 저장된 index 리턴


def Dijkstra(G):

    s = 0
    dist = [100000]*n
    dist[0]=0
    parent = ["None"]*n
    parent[0] = 0
    H = AdaptedHeap()

    for i in range(n):
        H.insert(dist[i])


    idx = 0
    while len(H) != 0:
        u = H.delete_min()
        if u!=0 and u == dist[idx]:
            idx = dist.index(u, idx+1)
        else:
            idx = dist.index(u)
        for i in G:
            if i[0][0] == idx:
                v = i[0][1]
                if dist[v] > dist[idx] + i[1]:
                    H.update_key(dist[v], dist[idx] + i[1])
                    dist[v] = dist[idx] + i[1]
                    parent[v] = u

    return dist,parent

n = int(input())
m = int(input())
G = []
for _ in range(m):
    B = [int(x) for x in input().split()]
    G.append([(B[0],B[1]),B[2]])

dist, parent = Dijkstra(G)

for i in range(n):
    if dist[i] == 100000:
        print("inf",end=' ')
    else:
        print(dist[i],end=' ')

