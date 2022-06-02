from ast import Delete
import math


class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        e = self.top.data
        self.top = self.top.link
        return e

    def push(self, e):
        newNode = Node(e)
        newNode.link = self.top
        self.top = newNode


class Queue:
    MAX_QSIZE = 100

    def __init__(self):
        self.items = [None]*Queue.MAX_QSIZE
        self.front = -1
        self.rear = -1
        self.size = 0

    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, e):
        if self.size == len(self.items):
            print("Queue is full")
            self.resize(2*len(self.items))
        else:
            self.rear = (self.rear+1) % (len(self.items))
            self.items[self.rear] = e
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front = (self.front+1) % (len(self.items))
            e = self.items[self.front]
            self.size -= 1
            return e

    def resize(self, cap):
        olditems = self.items
        self.items = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = olditems[walk]
            walk = (walk + 1) % len(olditems)
        self.front = -1
        self.rear = self.size - 1


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items == []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()

    '''
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
        '''

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.items[-1]


class LinkedQueue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, e):
        newNode = Node(e)
        if self.front == None:
            self.front = self.rear = newNode
        else:
            self.rear.link = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        e = self.front.data
        self.front = self.front.link
        return e


class ArrayList:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def insert(self, pos, elem):
        if pos < 0 or pos > self.size():
            print("위치 error")
            return None
        else:
            self. items.insert(pos, elem)
#이진트리 

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.link
        return count

    def recusize(self):
        return self.nodeCount(self.head)

    def nodeCount(self, node):
        if node == None:
            return 0
        else:
            return self.nodeCount(node.link)+1

    def insert(self, pos, elem):
        if pos < 0 or pos > self.size():
            print("위치 error")
            return
        node = Node(elem)
        before = self.getNode(pos-1)
        if before == None:
            node.link = self.head

            self.head = node
        else:
            node.link = before.link
            before.link = node

    def delete(self, pos):
        if pos < 0 or pos > self.size():
            print("위치 error")
            return None

        before = self.getNode(pos-1)
        if before == None:
            elem = self.head.data
            self.head = self.head.link
        else:
            elem = before.link.data
            before.link = before.link.link
        return elem

    def printList(self):
        node = self.head
        while node != None:
            e = node.data
            print("e")
            node = node.link

    def find(self, item):
        pos = 0
        node = self.head
        while node is not None:
            if item == node.data:
                return pos
            else:
                node = node.link
                pos += 1
        return -1


'''
n = int(input())
Wtime = Queue()
Itime = Queue()
for i in range(n):
    x, y = input().split()
    Wtime.enqueue(int(x))
    Itime.enqueue(int(y))
sum = 0
num = 0

for i in range(n-1):
    sum = sum + Itime.items[i] - Wtime.items[i+1]
    if sum < 0:
        sum = 0
    else:
        num = num + sum

num = num/n
num = round(num, 3)
print(format(num, ".2f"))
'''
a = Queue()
print(len(a.items))
