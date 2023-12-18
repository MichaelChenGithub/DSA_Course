"""
Implement quick sort in Python.
Input a list.
Output a sorted list.
"""
def quicksort(array, l, base):
    # keep the arr last index for recursive sub-quicksort
    r = base
    while l < base:
        if array[l] >= array[base]:
            array[l], array[base-1], array[base] = array[base-1], array[base], array[l]
            base-=1
        else:
            l += 1
        quicksort(array, 0, base-1)
        quicksort(array, base+1, r)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14] # [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
print(quicksort(test, 0, len(test)-1))
