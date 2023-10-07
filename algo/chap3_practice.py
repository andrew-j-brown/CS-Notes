list = [1, 2, 5, 6, 8, 19, 21, 35, 75]

def binary_search(list, n):
    first = 0
    last = len(list) - 1
    while last >= first:
        middle = (first + last) // 2
        if list[middle] == n:
            return True
        else:
            if n < list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return False

print(binary_search(list, 7))
print(binary_search(list, 21))
print(binary_search(list, 6))
