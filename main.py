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

import queue
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
        print(-L.queue[0], end = " ")
