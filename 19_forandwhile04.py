num = 0
for x in range(1, 1001):
    if x % 2 == 0:
        num = num + 1
print(num)


def count_numbers(start, end):
    return end - start


result = num
print(f"Total de números: {result}")
