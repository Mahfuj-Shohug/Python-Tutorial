# Iterator generator function
for i in range(10):
    print(i)

# Iterator Function
# as called helper function
print(range(0, 20, 2))


# Iterator vs 2 type generator -> 1. default iterator function. 2. custom iterator function
def my_range(endpoint):
    for i in range(endpoint):
        yield i


# Yield act as a iterator function or object
for i in my_range(10):
    print(i, end=" ")

print(my_range(100))

# Building function
# Map, Reduce, Filter
# Map(function, iterator)
print('-' * 100)
num = lambda x: x
print(list(map(num, [10, 20, 30, 40, 50])))
# map use for the single value using from the list

#reduce (Function , secquence or list)
from functools import reduce
print(reduce(lambda x,y: x+y, [10, 20, 30, 40, 50]))
print(reduce(lambda x,y: x if x<y else y, [10, 20, 30, 40, 50]))

#Filter function
def even_number(num):
    if num % 2 == 0:
        return True
    return False
res = filter(even_number, [1, 3, 4, 6, 7, 8, 9])
print(list(res))