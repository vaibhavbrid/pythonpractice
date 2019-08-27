from Node import Node

class LinkedList:
    def __init__(self):
        self.root = None

    root = Node
    head = Node

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            self.head = self.root
        else:
            self.head.next_node = newNode
            self.head = newNode

    def len(self):
        linkedListLenCounter = 0
        if self.root is not None:
            linkedListLenCounter += 1
            currentNode = self.root
            while currentNode.next_node is not None:
                linkedListLenCounter += 1
                currentNode = currentNode.next_node
            return linkedListLenCounter


    def print(self):
        if self.root is None:
            print(f'No nodes found')
        else:
            print(str(self.root.data) + "->" , end="")
            self.head = self.root
            while self.head.next_node is not None:
                print(str(self.head.next_node.data) + "->", end="")
                self.head = self.head.next_node
            if self.head.next_node is None:
                print("null")

    '''To remove the kth last element we maintain 2 variables. The previous, current and the kth element from the current'''
    def removeKthLastElement(self, kthElement):
        if kthElement > self.len():
            print('Input value lower than length')
        else:
            currentNode = self.root
            localKthNode = currentNode
            for i in range(kthElement-1):
                localKthNode = localKthNode.next_node
            while localKthNode.next_node is not None:
                previousNode = currentNode
                currentNode = currentNode.next_node
                localKthNode = localKthNode.next_node
            previousNode.next_node = currentNode.next_node
            currentNode.next_node = None
        return self



