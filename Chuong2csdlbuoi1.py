'''#ngay12/0/2022'''
#cau truc du lieu

'''from queue import *

#Q = Queue()
Q = PriorityQueue()

for x in [4,7,8,1,6,92]: Q.put(x)
while Q.qsize(): print(Q.get(), end = " ")
'''
'''import  queue
class item:
    def __init__(self): self.val=x
    def __lt__(self, other):
        return self.val< other.val if self.val%3 else self.val%3 < other.val%3
if __name__ == '__main__' :
    Q=queue.PriorityQueue()
    for x in [312, 142, 15, 1 ,2,6432,]: Q.put(item(x))
    while Q.qsize():
        print(Q.get().val, end = " ")'''

#phan tu trung vi

'''import queue
if __name__ == '__main__':
    L= queue.PriorityQueue()
    R= queue.PriorityQueue()
    n, *a = list(map(int,input().split()))
    for i,x in enumerate(a):
        if i%2 : R.put(x)
        else:L.put(-x)
        if i>0 and -L.queue[0] > R.queue[0]:
            u, v=L.get(), R.get()
            L.put(-v)
            R.put(-u)
        print(-L.queue[0], end = " ")'''

# 19.9.2022 Thuat toan BFS (Breadth First Search)  (dung queue)
# bai toan đong nước : có 2 can n, m lít . Đong K lít
#tuble vs list

    import queue
    class Water:
        P = {}
        def nhap(self):
            self.n, self.m, self.k = map(int, input().split())
        `def inkq(self,v):
            if v[0]
        def BFS(self):
            Q = queue.Queue()
            Q.put((0,0))
            self.P[(0,0)] = (-1,-1)
            while Q.qsize():
                x,y = Q.get()
                z=x+y
                Next=[(0,y), (x,0), (self.n,y), (x,self.m), (max(0,z-self.m)), (min(z, self.n), max(0,z-self.n))]
                for v in Next:
                    if v not in self.P.keys():
                        Q.put(v)
                        self.P[v]=(x,y)
                        if v[0] == self.k or v[1] == self.k:
                            self.inkq(v)
                            return
                print("khong dong duoc nuoc")

    if __name__ == '__main__'
        W=Water()
        W.Nhap()
        W.BFS()

