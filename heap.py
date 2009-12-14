

r"""

# Try constructing a heap and popping its elements

>>> h = Heap()
>>> h.add(5, "Foo")
>>> h.pop()
(5, 'Foo')
>>> h.empty()
True

# Intertwining insertions and deletions

>>> h = Heap()
>>> h.add(7, "Bar")
>>> h.add(15, "Baz")
>>> h.pop()
(7, 'Bar')
>>> h.pop()
(15, 'Baz')
>>> h.empty()
True
>>> h.add(9, "Bam")
>>> h.add(7, "Bar")
>>> h.add(15, "Baz")
>>> h.add(5, "Foo")
>>> h.pop()
(5, 'Foo')
>>> h.add(3, "Frap")
>>> h.pop()
(3, 'Frap')
>>> h.pop()
(7, 'Bar')
>>> h.add(8, "Murk")
>>> h.pop()
(8, 'Murk')
>>> h.pop()
(9, 'Bam')
>>> h.pop()
(15, 'Baz')

# Heapifying input

>>> h = Heap([(5,5),(9,9),(2,2),(8,8),(4,4),(6,6),(3,3),(1,1)])
>>> h.size()
8
>>> h.pop()
(1, 1)
>>> h.pop()
(2, 2)
>>> h.pop()
(3, 3)
>>> h.pop()
(4, 4)
>>> h.pop()
(5, 5)
>>> h.pop()
(6, 6)
>>> h.pop()
(8, 8)
>>> h.pop()
(9, 9)

"""

class Heap(object):
    _array = list([None])

    def _swap(self, index):
        parent_index = index / 2
        (self._array[index], self._array[parent_index]) = \
                (self._array[parent_index], self._array[index])

    def __init__(self, initial=None):
        if initial is None:
            self._array = [None]
        else:
            self._array = [None] + initial
            for i in xrange(len(initial) / 2, 0, -1):
                self._heapify(i)

    def _heapify(self, index):
        if index > len(self._array) / 2:
            return
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        if right_child_index < len(self._array):
            (min_value, min_index) = min(
                    (self._array[left_child_index][0],
                        left_child_index),
                    (self._array[right_child_index][0],
                        right_child_index))
            if min_value < self._array[index][0]:
                self._swap(min_index)
                self._heapify(min_index)
        elif left_child_index < len(self._array):
            if self._array[left_child_index][0] < \
                    self._array[index][0]:
                self._swap(left_child_index)
                self._heapify(left_child_index)

    def add(self, key, value):
        self._array.append((key, value))
        self._upheap(len(self._array) - 1)

    def _upheap(self, index):
        parent_index = index / 2
        if parent_index == 0:
            return
        if self._array[parent_index][0] > self._array[index][0]:
            self._swap(index)
            self._upheap(parent_index)

    def pop(self):
        if self.empty():
            raise IndexError, 'Can\'t pop from empty heap'
        try:
            return self._array[1]
        finally:
            self._array[1] = self._array[-1]
            self._array.pop()
            self._downheap(1)

    def _downheap(self, index):
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        if right_child_index < len(self._array):
            (min_value, min_index) = min(
                    (self._array[left_child_index][0],
                        left_child_index),
                    (self._array[right_child_index][0],
                        right_child_index))
            if min_value < self._array[index]:
                self._swap(min_index)
                self._downheap(min_index)
        else:
            if left_child_index < len(self._array):
                if self._array[left_child_index][0] < \
                        self._array[index][0]:
                    self._swap(left_child_index)

    def size(self):
        return len(self._array) - 1

    def empty(self):
        return len(self._array) == 1


