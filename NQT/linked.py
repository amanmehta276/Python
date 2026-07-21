class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)

head=Node(2)
head.next=Node(3)
head.next.next=Node(4)

print(head)