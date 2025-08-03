from xml.etree.ElementPath import prepare_child


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None


    def remove_data_by_index(self, index):
        current = self.head
        previous = None
        current_index = 0

        if index < 0:
            print("Index can't be negative range")
            return

        if index == 0 and current is not None:
            self.head = current.next
            current = None
            return


        while current and current_index < index:
            previous = current
            current = current.next
            current_index += 1

        if current is None:
            return


        previous.next = current.next
        current = None









    # 8 -> 5 -> 7 -> 6 -> 9 ->

    def print_data(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next





ll = LinkedList()

# print(ll.head)

ll.append(8)
ll.append(5)
ll.append(7)
ll.append(6)
ll.append(9)

# print(ll.head.data)
#
ll.print_data()
# print()
#
# # ll.prepend(15)
#
# ll.print_data()
# print()
#
# # print(ll.head.data)
#
# # 8 -> 5 -> 7 -> 6 -> 9 ->
#
# ll.delete(7)
print()
# ll.print_data()
print("#################################")
ll.remove_data_by_index(1)
print(ll.print_data())
# print(f"\nremove index element {ll.print_data()}")