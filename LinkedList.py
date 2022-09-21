from tkinter.messagebox import NO


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node 

    def insert_at_end(self, data):
        node = Node(data, None)
        itr = self.head
        while itr:
            if itr.next == None:
                itr.next = node
                break

            itr = itr.next

    
    def insert_after(self, wdata, adata):
        itr = self.head
        while itr:
            if itr.data == wdata:
                node = Node(adata, itr.next)
                itr.next = node
                break

            itr = itr.next


    def insert_before(self, wdata, adata):
        itr = self.head
        prevNode = None

        while itr:
            if itr.data == wdata:
                node = Node(adata, prevNode.next)
                prevNode.next = node
                break

            prevNode = itr
            itr = itr.next

    def display(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next






if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beg(1)
    ll.insert_at_beg(2)
    ll.insert_at_beg(3)

    ll.insert_at_end(4)

    ll.insert_after(4, 6)

    ll.insert_before(6, 5)

    ll.display()