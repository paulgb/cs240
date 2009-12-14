
r'''

>>> d = Dictionary()
>>> d.insert(4, "Foo")
>>> d.get(4)
'Foo'
>>> d.insert(9, "Bar")
>>> d.get(9)
'Bar'
>>> d.insert(21, "Baz")
>>> d.get(21)
'Baz'
>>> d.get(9)
'Bar'
>>> d.get(4)
'Foo'

'''

DEFAULT_SIZE = 17
SLOT_EMPTY = None
SLOT_REMOVED = (None,)

class Dictionary(object):
    def __init__(self, size=DEFAULT_SIZE):
        self._size = size
        self._table = [SLOT_EMPTY] * size

    def _hashfun(self, key):
        return hash(key) % self._size

    def _rehash(self, hash, key):
        return hash + 1 % self._size

    def insert(self, key, value):
        hash = self._hashfun(key)
        for i in xrange(0, self._size):
            if self._table[hash] is None:
                self._table[hash] = (key, value)
                return
            hash = self._rehash(hash, key)
        raise OverflowError, 'dictionary is full'

    def remove(self, key):
        pass

    def get(self, key):
        hash = self._hashfun(key)
        for i in xrange(0, self._size):
            if self._table[hash] == SLOT_EMPTY:
                raise KeyError, key
            if self._table[hash] != SLOT_REMOVED:
                k, v = self._table[hash]
                if key == k:
                    return v
                else:
                    hash = self._rehash(hash, key)
        raise KeyError, key

    def element(self, key):
        pass

