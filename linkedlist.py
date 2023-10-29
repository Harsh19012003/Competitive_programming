class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0



    def push(self, node):
        if self.head == None:
            self.head = node
            self.size += 1
        else:
            x = self.head
            # print(x)
            while(x.next != None):
                x = x.next

            x.next = node
            self.size += 1



    def size_check(self):
        print(self.size)



    def traverse(self):
        x = self.head
        while(x != None):
            print(x.value, end="  ")
            x = x.next
        print(x)
        print("the end")
        
        print(end="\n")

    def popping(self):
        if self.head == None:
            return False
        else:
            x = self.head()
            while(x.next != None):
                y = x
                x = x.next
        # clean memory of node
            y.next = None
            size -= 1




node3 = Node(30)
node4 = Node(4000)

# print(id(node3))
# print(id(node4))


ll = LinkedList()

ll.push(node3)
# print(ll.head.value)


ll.push(node4)


node5 = Node(50)
ll.push(node5)



node6 = Node(50)
ll.push(node6)


ll.traverse()


ll.size_check()

ll.popping()
ll.traverse()
ll.size_check()