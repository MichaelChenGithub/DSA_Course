def binary_search(input_array, value):
    """
    input_array -> arr perhaps has the value
    value -> target we want its index
    """
    #l -> min index of scaled array
    l = 0
    # r -> max index of scaled array
    r = len(input_array)-1
    # mid_idx -> middle index of scaled array
    mid_idx = 0
    
    while l <= r:
        # calculate middle index -> n/2
        mid_idx = (r+l)//2
        if value > input_array[mid_idx]:
            l = mid_idx+1
        elif value < input_array[mid_idx]:
            r = mid_idx-1
        else:
            return mid_idx
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1)) # -1
print(binary_search(test_list, test_val2)) # 4