mat = [1, 2, 3, 4, 5]
result = [x for x in mat if x < 3]
print(result)

result = [x**3 for x in mat if 2 < x < 5]
print(result)


import random
result = [random.random() for _ in range(3)]
print(result)

result = [x for x in [random.random() for _ in range(10)] if x >= 0.5]
print(result)

result = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
print(result)
