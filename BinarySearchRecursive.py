def binary_search(input_array, value, l, r):
    """
    input_array -> arr perhaps has the value
    value -> target we want its index
    l -> min index of scaled array
    r -> max index of scaled array
    """
    if r >= l:
        # calculate middle index -> n/2
        mid_idx = (r+l)//2
        if input_array[mid_idx] == value:
            return mid_idx
        elif value > input_array[mid_idx]:
            return binary_search(input_array, value, mid_idx+1, r)
        elif value < input_array[mid_idx]:
            return binary_search(input_array, value, l, mid_idx-1)
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
# set initial left & right index for recursive
init_l = 0
init_r = len(test_list)-1
print(binary_search(test_list, test_val1, init_l, init_r)) # -1
print(binary_search(test_list, test_val2, init_l, init_r)) # 4