

r'''

>>> h = Heap()
>>> h.add(5, "Foo")
>>> h.pop()
(5, 'Foo')
>>> h.empty()
True
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

'''

class Heap(object):
    _array = list([None])

    def add(self, key, value):
        self._array.append((key, value))
        self._upheap(len(self._array) - 1)

    def _upheap(self, index):
        parent_index = index / 2
        if parent_index == 0:
            return
        if self._array[parent_index][0] > self._array[index][0]:
            (self._array[parent_index], self._array[index]) = \
                    (self._array[index], self._array[parent_index])
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
        if left_child_index < len(self._array) and \
                self._array[left_child_index] < self._array[index]:
            (self._array[left_child_index], self._array[index]) = \
                    (self._array[index], self._array[left_child_index])
            self._downheap(left_child_index)
        elif right_child_index < len(self._array) and \
                self._array[right_child_index] < self._array[index]:
            (self._array[right_child_index], self._array[index]) = \
                    (self._array[index], self._array[right_child_index])
            self._downheap(right_child_index)

    def size(self):
        pass

    def empty(self):
        return len(self._array) == 1


