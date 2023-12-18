# Average Case: O(n log n)
# Worst Case: O(n^2)
def quicksort(array, l, r):
    if l < r:
        base = partition(array, l, r)
        quicksort(array, l, base - 1)
        quicksort(array, base + 1, r)
    return array

def partition(array, l, r):
    pivot = array[r]
    i = l - 1

    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test) - 1))