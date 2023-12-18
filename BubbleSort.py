# O(n^2)
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([22, 46, 1, 33, 42, 24]))
print(bubble_sort([22, 22, 16, 33]))
print(bubble_sort([]))