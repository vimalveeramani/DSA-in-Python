def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + equal + quick_sort(right)

# Example usage:
my_list = [5, 2, 8, 12, 3]
sorted_list = quick_sort(my_list)
print(sorted_list)
