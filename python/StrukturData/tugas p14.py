def bubble_sort(arr, ascending=True):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr, ascending=True):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        extreme_index = i
        for j in range(i+1, n):
            if (ascending and arr[j] < arr[extreme_index]) or (not ascending and arr[j] > arr[extreme_index]):
                extreme_index = j
        arr[i], arr[extreme_index] = arr[extreme_index], arr[i]
    return arr

def insertion_sort(arr, ascending=True):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((ascending and arr[j] > key) or (not ascending and arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr, ascending=True):
    arr = arr.copy()
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid], ascending)
        right = merge_sort(arr[mid:], ascending)

        result = []
        while left and right:
            if (ascending and left[0] < right[0]) or (not ascending and left[0] > right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left + right
        return result
    return arr

def quick_sort(arr, ascending=True):
    arr = arr.copy()
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x < pivot if ascending else x > pivot)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if (x > pivot if ascending else x < pivot)]
    return quick_sort(left, ascending) + middle + quick_sort(right, ascending)


original_array = [8, 3, 10, 12, 7, 0, 9]
print("Array sebelum diurutkan:", original_array)

def display_sorted_results(sort_func, name):
    print(f"\n{name} Sort:")
    print("Ascending :", sort_func(original_array, ascending=True))
    print("Descending:", sort_func(original_array, ascending=False))

display_sorted_results(bubble_sort, "Bubble")
display_sorted_results(selection_sort, "Selection")
display_sorted_results(insertion_sort, "Insertion")
display_sorted_results(merge_sort, "Merge")
display_sorted_results(quick_sort, "Quick")