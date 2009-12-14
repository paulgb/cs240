

r"""

>>> sorted(last_occurrence('abcab').items())
[('a', 4), ('b', 5), ('c', 3)]
>>> last_occurrence('abcab')['d']
-1

>>> boyer_moore('the quick brown fox', 'quick')
4
>>> boyer_moore('the quick brown fox', 'fox')
16
>>> boyer_moore('the quick brown fox', 'the')
0
>>> boyer_moore('the quick brown fox', 'pants')
-1

"""

from collections import defaultdict

def last_occurrence(str):
    last = defaultdict(lambda: -1)
    for i, c in enumerate(str):
        last[c] = i + 1
    return last

def boyer_moore(haystack, needle):
    last = last_occurrence(needle)
    m = len(needle)
    i = m - 1
    j = m - 1
    while i < len(haystack):
        if haystack[i] == needle[j]:
            if j == 0:
                return i
            else:
                i = i - 1
                j = j - 1
        else:
            l = last[haystack[i]]
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1

