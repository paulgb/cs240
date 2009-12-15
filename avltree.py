
r"""
Note: the restructuring method is buggy
"""

r"""

>>> avl = AVLTree()
>>> avl.add(6)
>>> avl.contains(6)
True
>>> avl.contains(5)
False

>>> avl = AVLTree()
>>> avl.add(9)
>>> avl.add(3)
>>> avl.add(7)
>>> avl.add(1)
>>> avl.add(8)
>>> avl.add(3)
>>> map(avl.contains, range(1,10))
[True, False, True, False, False, False, True, True, True]

>>> avl = AVLTree()
>>> avl.add(3)
>>> avl.add(4)
>>> avl.add(5)
>>> avl.height()
1
>>> avl.contains(3)
True
>>> avl.contains(4)
True
>>> avl.contains(5)
True

>>> avl = AVLTree()
>>> avl.add(5)
>>> avl.add(4)
>>> avl.add(3)
>>> avl.height()
1
>>> avl.contains(3)
True
>>> avl.contains(4)
True
>>> avl.contains(5)
True

>>> from random import shuffle
>>> rands = range(100)
>>> #shuffle(rands)
>>> map(avl.add, rands) and None
>>> all(map(avl.contains, range(100)))
True
>>> avl.root.print_tree()

"""

class ReplaceNode(Exception):
    def __init__(self, node, replacement):
        self.node = node
        self.replacement = replacement


class AVLNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "node (%s)" % self.val

    def height(self):
        if self.left is not None:
            lh = 1 + self.left.height()
        else:
            lh = 0
        if self.right is not None:
            rh = 1 + self.right.height()
        else:
            rh = 0
        return max(lh, rh)

    def rebalance(self, path):
        if path[0].val < path[1].val:
            if path[1].val < path[2].val:
                left = AVLNode(path[0].val, path[0].left, path[1].left)
                right = path[2]
                parent = AVLNode(path[1].val, left, right)
                raise ReplaceNode(path[0], parent)
            else:
                left = AVLNode(path[0].val, path[0].left, path[2].left)
                right = AVLNode(path[1].val, path[2].right, path[1].right)
                parent = AVLNode(path[2].val, left, right)
                raise ReplaceNode(path[0], parent)
        elif path[0].val > path[1].val:
            if path[1].val > path[2].val:
                left = path[2]
                right = AVLNode(path[0].val, path[1].right, path[0].right)
                parent = AVLNode(path[1].val, left, right)
                raise ReplaceNode(path[0], parent)
            else:
                left = AVLNode(path[1].val, path[1].left, path[2].left)
                right = AVLNode(path[0].val, path[2].right, path[0].right)
                parent = AVLNode(path[2].val, left, right)
                raise ReplaceNode(path[0], parent)

    def print_tree(self):
        return "node (%s) [%s, %s]" % (self.val,
                self.left and self.left.print_tree(),
                self.right and self.right.print_tree())

    def insert(self, value, path):
        try:
            path += [self]
            if value > self.val:
                if self.right is None:
                    self.right = AVLNode(value)
                    path += [self.right]
                else:
                    self.right.insert(value, path)
                    return
            else:
                if self.left is None:
                    self.left = AVLNode(value)
                    path += [self.left]
                else:
                    self.left.insert(value, path)
                    return
            if len(path) >= 3:
                self.rebalance(path[-3:])
        except ReplaceNode, rn:
            if self.left == rn.node:
                self.left = rn.replacement
            elif self.right == rn.node:
                self.right = rn.replacement
            else:
                raise


class AVLTree(object):
    root = None

    def height(self):
        if self.root is None:
            return None
        else:
            return self.root.height()

    def add(self, value):
        try:
            if self.root is None:
                self.root = AVLNode(value)
            else:
                self.root.insert(value, [])
        except ReplaceNode, rn:
            if self.root == rn.node:
                self.root = rn.replacement
    
    def contains(self, value):
        node = self.root
        while node is not None:
            if node.val == value:
                return True
            elif node.val > value:
                node = node.left
            else:
                node = node.right
        return False

