def find_even_index(arr):

    for index, number in enumerate(arr):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return 0


find_even_index([1, 2, 3, 4, 3, 2, 1])
