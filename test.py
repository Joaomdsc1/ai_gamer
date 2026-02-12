x = int(input("digite o numero que será calculado o fatorial: "))
fat = x
for i in range(x - 1):
    fat = fat * (x - 1)
    x -= 1

print(fat)

