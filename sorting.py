def swap(arr, index_one, index_two):
    """Swaps place of two entries in an array."""
    temp = arr[index_one]
    arr[index_one] = arr[index_two]
    arr[index_two] = temp
    return arr

def insertion_sort(arr):
    """Returns sorted array using insertion sort."""
    for i in range(len(arr)):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j = j - 1
    return arr
