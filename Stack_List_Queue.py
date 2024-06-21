class Node():
    def __init__(self, v):
        self.value = v
        self.next = None


class List():

    def __init__(self):
        self.tail = None
        self.root = None


    def AddRoot(self, node):
        node.next = self.root
        if self.tail is None:
            self.tail = node
        self.root = node


    def AddTail(self, node):

        if self.tail is None:
            self.root = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def RemoveRoot(self):
        to_remove = self.root
        self.root = self.root.next
        if self.tail == to_remove:
            self.tail = None
        return to_remove

    def At(self, index):
        current = self.root
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def RemoveIndex(self, index):
        if index == 0:
            return self.RemoveRoot()
        current = self.At(index - 1)
        to_remove = current.next
        current.next = to_remove.next
        if self.tail == to_remove:
            self.tail = current
        return to_remove

    def RemoveTail(self):
        if self.root == self.tail:
            return self.RemoveRoot()
        current = self.root
        while current.next != self.tail:
            current = current.next
        to_remove = self.tail
        current.next = None
        self.tail = current
        return to_remove

    def Print(self):
        current = self.root
        while (current != None):
            print(current.value)
            current = current.next
        # print(self.tail.value)

    def Find(self, value):
        current = self.root
        while current.next.value != value:
            if current == None:
                return None
            current = current.next
        return current

    def Remove(self, value):
        if self.root.value == value:
            return self.RemoveRoot()
        current = self.root
        while current.next.value != value:
            current = current.next
        to_remove = current.next
        current.next = to_remove.next
        if self.tail == to_remove:
            self.tail = current
        return to_remove


class Queue():
    def __init__(self):
        self.list = List()

    def push(self, value):
        node = Node(value)
        self.list.AddTail(node)

    def pop(self):
        current = self.list.RemoveIndex(0)
        return current.value


class Stack():
    def __init__(self):
        self.list = List()

    def push(self, value):
        node = Node(value)
        self.list.AddTail(node)

    def pop(self):
        current = self.list.RemoveTail()
        return current.value


class Queue_on_array():
    def __init__(self):
        self.container = [0] * 10
        self.i_push = 0
        self.i_pop = 0

    def Push(self, value):
        if self.i_pop + len(self.container) == self.i_push:
            lenght = len(self.container)
            i = self.i_pop % lenght
            arr = [0] * (lenght * 2)
            arr[:i] = self.container[:i]
            arr[lenght + i + 1:] = self.container[i + 1:]
            self.container = arr
            self.i_pop = i + lenght
            self.i_push = self.i_pop + lenght
        self.container[self.i_push % len(self.container)] = value
        self.i_push += 1

    def Pop(self):
        if self.Empty():
            return None
        value = self.container[self.i_pop % len(self.container)]
        self.i_pop += 1
        return value

    def Empty(self):
        return self.i_pop == self.i_push

