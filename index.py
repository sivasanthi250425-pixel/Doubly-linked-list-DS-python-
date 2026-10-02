
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    # Delete from position
    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(1, position):
            temp = temp.next

        if temp.next is None:
            self.delete_end()
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # Search
    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                print("Element found")
                return

            temp = temp.next

        print("Element not found")

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" ⇄ ")
            temp = temp.next

        print("None")

    # Check empty
    def is_empty(self):
        return self.head is None


# Create list
list = DoublyLinkedList()


# Menu
while True:
    print("\n--- DOUBLY LINKED LIST ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Search")
    print("8. Display")
    print("9. Is Empty")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        list.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        list.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        list.insert_position(data, position)

    elif choice == 4:
        list.delete_beginning()

    elif choice == 5:
        list.delete_end()

    elif choice == 6:
        position = int(input("Enter position: "))
        list.delete_position(position)

    elif choice == 7:
        key = int(input("Enter element to search: "))
        list.search(key)

    elif choice == 8:
        list.display()

    elif choice == 9:
        if list.is_empty():
            print("List is empty")
        else:
            print("List is not empty")

    elif choice == 10:
        print("Program ended")
        break

    else:
        print("Invalid choice")

