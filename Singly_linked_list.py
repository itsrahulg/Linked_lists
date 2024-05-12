class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_linked_list:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty linked list")
        else:
            starting = self.head
            while starting is not None:
                print(starting.data, end=" --> ")
                starting = starting.next
            print("null")

    def add_first(self,element):
        newnode = Node(element)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def add_last(self,element):
        newnode = Node(element)
        if self.head is None:
            self.head = newnode
        else:
            starting = self.head
            while starting.next is not None:
                starting = starting.next
            starting.next = newnode

    def add_at_position(self,element,position):
        newnode = Node(element)
        for i in range(1,position-1):
            starting = starting.next
        newnode.next = starting.next
        starting.next = newnode

    def delete_first(self):
        if self.head is None:
            print("empty linked list")
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("empty linked list")
        else:
            starting = self.head
            while starting.next.next is not None:
                starting = starting.next
            starting.next = None

    def delete_at_position(self,position):
        if self.head is None:
            print("empty list")
        else:
            starting = self.head
            for i in range(1, position-1):
                starting = starting.next
            starting.next = starting.next.next


linked_list = Singly_linked_list()
N = int(input())
for i in range(N):
    num = int(input())
    linked_list.add_last(num)

linked_list.display()










