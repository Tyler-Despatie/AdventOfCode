
from sys import stdin
from re import search

inputs = stdin.read().split()

print("Part 1:")
print(len([x for x in inputs if search("((a|e|i|o|u).*){3,}", x) and search("(\w)\\1", x) and not search("ab|cd|pq|xy", x)]))

print("Part 2:")
print(len([x for x in inputs if search("(\w\w).*\\1", x) and search("(\w).\\1", x)]))