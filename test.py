arr = [1, 2, 3]
arr2 = map(lambda x: x + 2 if x % 2 == 0 else (x + 5 if x > 2 else x), arr)
print(list(arr2))
