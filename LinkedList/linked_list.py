class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self.length = 0
        if values:
            for value in values:
                self.push(value)

    def __len__(self):
        return self.length

    def head(self):
        if self.__len__() == 0:
            raise EmptyListException("The list is empty.")
        
        return self._head

    def push(self, value):
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node
        self.length += 1

    def pop(self):
        if self.__len__() == 0:
            raise EmptyListException("The list is empty.")
        
        to_return = self._head
        self._head = self._head._next

        self.length -= 1

        return to_return._value

    def reversed(self):
        values = []
        current = self._head
        
        for _ in range(self.__len__()):
            values.append(current.value())
            current = current._next

        return LinkedList(values)

    def __iter__(self):
        current = self._head

        while current:
            yield current._value
            current = current._next


class EmptyListException(Exception):
    pass
