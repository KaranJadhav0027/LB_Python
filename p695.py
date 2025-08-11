
class Node:
    def __init__(self,No):
        self.Data=No
        self.next=None

def main():
    print("Demonstration of Singly Linear Linked List")

    obj1=Node(11)
    obj2=Node(21)
    obj3=Node(51)

    obj1.next=obj2
    obj2.next=obj3
    obj3.next=None

    head=obj1
    print(head.Data) #11

    head=head.next
    print(head.Data)  #21

    head=head.next
    print(head.Data)  #51

if __name__=="__main__":
    main()