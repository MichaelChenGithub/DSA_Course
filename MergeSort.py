# O(n log n)
def merge_sort(arr):
    # 檢查陣列是否只有一個元素或是空的
    if len(arr) <= 1:
        return arr
    
    # 找到陣列的中間位置
    mid = len(arr) // 2
    
    # 將陣列分成左右兩部分
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 遞迴對左右兩部分進行 merge_sort
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 合併兩個已排序的子陣列
    return merge(left_half, right_half)

def merge(left, right):
    result = []  # 用於存放合併後的結果
    i = j = 0  # 用於遍歷左右兩個子陣列的指標
    
    # 比較左右兩個子陣列的元素，將較小的元素加入結果中
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 將剩餘的元素加入結果中
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 測試
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("原始陣列:", arr)
print("排序後陣列:", sorted_arr)
