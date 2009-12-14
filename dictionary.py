
r'''

>>> d = Dictionary(7)
>>> d.element(4)
False
>>> d.insert(4, "Foo")
>>> d.element(4)
True
>>> d.get(4)
'Foo'
>>> d.insert(9, "Bar")
>>> d.get(9)
'Bar'
>>> d.insert(11, "Baz")
>>> d.get(11)
'Baz'
>>> d.get(4)
'Foo'
>>> sorted(d.keys())
[4, 9, 11]
>>> sorted(d.values())
['Bar', 'Baz', 'Foo']
>>> d.remove(4)
>>> d.element(4)
False
>>> d.get(11)
'Baz'

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
        hash = self._hashfun(key)
        for i in xrange(0, self._size):
            if self._table[hash] == SLOT_EMPTY:
                raise KeyError, key
            if self._table[hash] != SLOT_REMOVED:
                k, v = self._table[hash]
                if key == k:
                    self._table[hash] = SLOT_REMOVED
                    return
                else:
                    hash = self._rehash(hash, key)
        raise KeyError, key

    def get(self, key):
        hash = self._hashfun(key)
        for i in xrange(0, self._size):
            if self._table[hash] == SLOT_EMPTY:
                raise KeyError, key
            if self._table[hash] != SLOT_REMOVED:
                k, v = self._table[hash]
                if key == k:
                    return v
            hash = self._rehash(hash, key)
        raise KeyError, key

    def element(self, key):
        try:
            self.get(key)
        except KeyError:
            return False
        return True

    def keys(self):
        keys = []
        for slot in self._table:
            if slot not in (SLOT_EMPTY, SLOT_REMOVED):
                key, value = slot
                keys.append(key)
        return keys

    def values(self):
        values = []
        for slot in self._table:
            if slot not in (SLOT_EMPTY, SLOT_REMOVED):
                key, value = slot
                values.append(value)
        return values

