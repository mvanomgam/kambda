# one line anonymous function defined without a name as as follows:
# lambda arguments: expression

add10 = lambda x: x + 10
print(f"\n{add10(5)}")

mult = lambda x, y: x*y
print(f"\n{mult(2,7)}")

# usese of lambda functions:
# 1. Sorted function

points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sort = sorted(points)

# by default, the sort is based on the 1st element of the tuple 
print(f"\n{points}")
print(f"{points_sort}")

# sort by the 2nd element of the tuple
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sort = sorted(points, key=lambda x: x[1])

print(f"\n{points}")
print(f"{points_sort}")

# sort by the sum of elements of teh tuple
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sort = sorted(points, key=lambda x: x[0] + x[1])

print(f"\n{points}")
print(f"{points_sort}")

# 2. Map function

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)

print(f"\n{a}")
print(f"{list(b)}")

# alternatively use list comprehension:
c = [x*2 for x in a]
print(f"\n{a}")
print(c)

# 3. Filter function 

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)

print(f"\n{a}")
print(f"{list(b)}")

# alternatively use list comprehension:
c = [x for x in a if x % 2 == 0]
print(f"\n{a}")
print(c)

# 4. Reduce function
from functools import reduce

a = [1, 2, 3, 4]
prod = reduce(lambda x, y: x*y, a)
print(f"\n{prod}")