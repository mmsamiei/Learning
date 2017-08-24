res = {x: x**2 for x in range(10)}
print(res)

res = {x: x*3 for x in range(10) if x % 2 == 1}
print(res)

res = {x: [y for y in range(0, x)] for x in range(6)}
print(res)
