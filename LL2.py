class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')

            temp = temp.next
    print()

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return None

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteFromBeginning(self):
        if self.head is None:
            return "The List is Empty"
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            return "List is Empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, value):

        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"Value '{value}' found at position {position}"
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list"


if __name__ == "__main__":
    llist = LinkedList()

    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")

    llist.printLinkedList()

    llist.deleteFromBeginning()
    print("\nList after deletion: ")
    llist.printLinkedList()

    llist.insertAtTheEnd("Jumps")
    #llist.printLinkedList()
    llist.insertAtTheEnd("Over")
    llist.insertAtTheEnd("The")
    llist.insertAtTheEnd("Lazy")
    llist.insertAtTheEnd("Dog")
    llist.printLinkedList()
    print("\n")
    print(llist.search('Quick'))
    print(llist.search('Lazy'))
