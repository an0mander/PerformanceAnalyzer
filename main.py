import random
import time

'''
Insertion Sort Algorithm
'''
def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key - 1]:
            wk_key = key
            while wk_key > 0 and arr[wk_key] < arr[wk_key - 1]:
                arr[wk_key], arr[wk_key - 1] = arr[wk_key - 1], arr[wk_key]
                wk_key -= 1
                return (arr)
                # print(arr)

'''
Quick Sort Algorithm
'''
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)


'''
Merge Sort Helper Function 
'''
def merge_sorted(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    # print(sorted_arr)
    return sorted_arr

'''
Mergesort Algorithm
'''
def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)

'''
Bubblesort Algorithm
'''
def bubblesort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num]

'''
Random List Generator
'''
def list_gen(begin, end, size):
    random_list = random.sample(range(begin_range, end_range), list_size)
    # print(random_list)
    return random_list

'''
Sorting Algorithm Analyser 
'''
def analyze_func(function_name, arr):
    tic = time.time()
    function_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{function_name.__name__.capitalize()}\t Elapsed time -> {seconds:.5f}")


'''
Driver Code
'''
list_size = int(input("Enter list size: "))
begin_range = int(input("Enter begin range: "))
end_range = int(input("Enter end range: "))
repeat = int(input("How many times do you want to repeat?: "))

for i in range(repeat):
    arr = list_gen(list_size, begin_range, end_range)
    analyze_func(bubblesort, arr.copy())
    analyze_func(quicksort, arr)
    analyze_func(mergesort, arr)
    analyze_func(sorted, arr)
    print('-' * 60)
