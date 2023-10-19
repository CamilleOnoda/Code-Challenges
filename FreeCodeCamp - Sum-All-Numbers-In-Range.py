# Travis' solution
def sumAll(lst):
    highest = max(lst)
    lowest = min(lst)

    total = 0

    while lowest <= highest:
        total += lowest
        lowest += 1

    return total

result = sumAll([1, 10])
print(result)

# My solution
def sumAll(lst):
    start, end = min(lst), max(lst)
    total = sum(range(start, end + 1))
    return total

result = sumAll([40, 4])
print(result)