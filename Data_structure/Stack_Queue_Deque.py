class Stack:
    """
    A class representing a stack data structure.

    This class implements a stack using a list, where items are appended and popped from the end of the list.

    Methods:
        push(item):
            Adds an item to the top of the stack.

        pop():
            Removes and returns the top item from the stack.

        peek():
            Returns the top item from the stack without removing it.

        size():
            Returns the number of items in the stack.

        is_empty():
            Returns a boolean indicating whether the stack is empty.

        printStack():
            Prints all the items in the stack, separated by arrow symbols.

    """

    def __init__(self):
        """
        Initializes a new instance of the Stack class.

        This constructor creates an empty list to store the stack items.
        """
        
        self.items = []

    def push(self, item):
        '''Accepts item as a parameter and appends it to a list.
        Returns nothing

        The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens in constant time
        '''

        self.items.append(item)

    def pop(self):
        """Removes and returns the last item from the list, which is also the
        top item of the stack

        Runtime here is constant time, O(1) because all it does is index to the
        last item and remove it
        """

        if self.items:  # if self.items
            return self.items.pop()

    def peek(self):
        """Peeks the last item of the list and returns it, the top item of the stack

        Runtime here is constant time because indexing into a list is done
        in constant time O(1)
        """
        if self.items:
            return self.items[-1]

    def size(self):
        """This method returns the length of the list that is representing the Stack.add()

        Runtime is constant time O(1) because finding the length of a list is constant
        """
        return len(self.items)

    def is_empty(self):
        """This method returns a boolean value describing whether or not the 
        Stack is empty

        Runtime is constant as testing for equality happens in constant time
        """
        return self.items == []
    
    def printStack(self):
        """Prints all the items in the stack by iterating through them and creating a string with arrow separators between each item. 
        Returns nothing.
        
        The runtime of this is O(n) or constant time as we are iterating each item
        of the list and printing them
        """
        main_str = ""
        for item in self.items:
            main_str += str(item) + "--> "
        print(main_str)


class Queue:
    """
    A class representing a queue data structure.

    This class implements a queue using a list, where items are inserted at the 0th index and removed from the end of the list.

    Methods:
        enqueue(item):
            Adds an item to the back of the queue.

        dequeue():
            Removes and returns the front-most item from the queue.

        peek():
            Returns the front-most item from the queue without removing it.

        size():
            Returns the number of items in the queue.

        is_empty():
            Returns a boolean indicating whether the queue is empty.

    """

    def __init__(self):
        """
        Initializes a new instance of the Queue class.

        This constructor creates an empty list to store the queue items.
        """
        
        self.items = []

    def enqueue(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.

        The runtime is O(n) or linear time, because inserting into the 0th index of a 
        list forces all the other itmes in the list to move one index to the right.
        """

        self.items.insert(0, item)

    def dequeue(self):
        """Returns and removes the front most item of the Queue, which is represented by
        the last item in the list.

        The runtime of this is O(n) or constant time as we are removing items from the end
        of the list
        """
        if self.items:
            return self.items.pop()

    def peek(self):
        """Returns the last item in the list, which represents the front most item
        in the queue.

        The runtime is constant because we're just indexing to the last item of the
        list and returning the value found there.
        """
        if self.items:
            return self.items[-1]

    def size(self):
        '''Returns the size of the Queue, represented bylength of the list

        Runtime is O(1) or constant time, because we're only returning the length'''
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value expressing whether or not the list representing the
        queue is empty

        Runs in constant time as it is only checking equality
        """
        return self.items == []


class Deque:
    """
    A class representing a deque (double-ended queue) data structure.

    This class implements a deque using a list, allowing items to be added or removed from both ends of the deque.

    Methods:
        add_front(item):
            Adds an item to the front of the deque.

        add_rear(item):
            Adds an item to the rear of the deque.

        remove_front():
            Removes and returns the front-most item from the deque.

        remove_rear():
            Removes and returns the rear-most item from the deque.

        peek_front():
            Returns the front-most item from the deque without removing it.

        peek_rear():
            Returns the rear-most item from the deque without removing it.

        size():
            Returns the number of items in the deque.

        is_empty():
            Returns a boolean indicating whether the deque is empty.
    """

    def __init__(self):
        """
        Initializes a new instance of the Deque class.

        This constructor creates an empty list to store the deque items.
        """
        
        self.items = []

    def add_front(self, item):
        """Takes an item as a parameter and inserts it into the 0th index
        of the list that is representing the Deque.

        The runtime is linear, or O(n), because every time you insert into the
        front of a list, all the other items in the list need to shift one
        position to the right.
        """

        self.items.insert(0, item)

    def add_rear(self, item):
        """Takes in an item as aparameter and appends that item to the end of
        the list that is representing the Deque.

        The runtime is constant because appending to the end of a list happens
        in constant time.
        """

        self.items.append(item)

    def remove_front(self):
        """Removes and returns the item in the 0th index of the list, which
        represents the front of the Deque.

        The runtime is linear, or O(n), because when we remove an item from the
        0th index, all the other items have to shift one index to the left.
        """

        if self.items:
            return self.items.pop(0)

    def remove_rear(self):
        """Removes and returns the last item of the list, which represents the
        rear of the Deque.

        The runtime is constant because all we're doing is indexing to the end
        of a list.
        """

        if self.items:
            return self.items.pop()

    def peek_front(self):
        """Returns the value found at the 0th index of the list, which represents
        the front of the Deque.

        The runtime is constant because all we're doing is indexing into a list.
        """

        if self.items:
            return self.items[0]

    def peek_rear(self):
        """Returns the value found at the 1st, or last, index.

        The runtime is constant because all we're doing is indexing into a
        list."""
        if self.items:
            return self.items[-1]

    def size(self):
        """Returns the length of the list, which is representing the Deque.

        The runtime will be constant because all we're doing is finding the length
        of a list and returning that value."""

        return len(self.items)

    def is_empty(self):
        """Checks to see if the list representing our Deque is empty. Returns True
        if it is, or False if it isn't.

        The runtime is constant because all we're doing is comparing two values.
        """
        return self.items == []
