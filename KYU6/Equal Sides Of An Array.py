def find_even_index(arr):

    for index, number in enumerate(arr):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return -1


find_even_index([1, 2, 3, 4, 3, 2, 1])

print(reversed(list(range(1, 11))))
