"""A deque is a double-ended queue. It can be used to add or remove elements from both ends. Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction. The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end."""

from collections import deque

d = deque()

# append() : add elements to the right end
d.append("a")
d.append("b")
print(d)  # deque(['a', 'b'])

# appendleft() : add elements to the left end
d.appendleft("c")
print(d)  # deque(['c', 'a', 'b'])

# pop() : return and remove elements from the right
print(d.pop())  # b
print(d)  # deque(['c', 'a'])

# popleft() : return and remove elements from the left
print(d.popleft())  # c
print(d)  # deque(['a'])

# clear() : remove all elements
d.clear()
print(d)  # deque([])

d = deque(["a", "b", "c", "d"])

# extend at right or left side
d.extend(["e", "f", "g"])
d.extendleft(["h", "i", "j"])  # note that 'j' is now at the left most position
print(d)  # deque(['j', 'i', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

# count(x) : returns the number of found elements
print(d.count("h"))  # 1

# rotate 1 positions to the right
d.rotate(1)
print(d)  # deque(['g', 'j', 'i', 'h', 'a', 'b', 'c', 'd', 'e', 'f'])

# rotate 2 positions to the left
d.rotate(-2)
print(d)  # deque(['i', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'j'])
