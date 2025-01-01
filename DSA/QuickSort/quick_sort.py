# Quick sort is an sorting algorithms.
# Quick sort follows the divide and conquer method to sort an elements.


'''
# Algorithms:
arr =  [ 10, 16, 8, 12, 15, 3, 9, 6 ]
------------------------------------------------------
step 1: select pivot element.
    Question: How to select the pivot element ?
        a. Randomly.
        b. Median.
        c. 1st element.
        d. Last element.
    Usually, we take last element as 'Pivot' element.
    pivot_element = 6
    Our Jobs is to arrange the elements on the basis of the
    pivot-element.
    If other_element < pivot_element => arrange at left.
    If other_element > pivot_element => arrange at right.

step 2:
------------------------------------------------------
'''


def partition(arr, low, high):
    # Taking an last element as pivot element.
    pivot_element = arr[high]
    # 'i' to track the how much elements will come less than pivot element.
    # Assuming that there are no any element lesser than pivot element.
    i = low - 1

    #
    for j in range(low, high):
        
        if arr[j] < pivot_element:
            i = i + 1
            # Swap
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    #
    i = i + 1
    temp = arr[i]
    arr[i] = pivot_element
    arr[high] = temp
    return i  # return pivot index.


def quick_sort(arr, low, high):
    if low < high:
        pivot_element = partition(arr, low, high)
        # once, we found the correct position of the pivot element, then
        # We have to sort the left element less than pivot and right element
        # greater than pivot.

        # CASE 1: sorting elements less than pivot element.
        quick_sort(arr, low, pivot_element - 1)

        # CASE 2: sorting elements greater than pivot element.
        quick_sort(arr, pivot_element+1, high)


if __name__ == "__main__":
    print("\nQuick-Sort-Implementation\n")
    arr = [10, 16, 8, 12, 15, 3, 9, 6]
    n = len(arr)
    quick_sort(arr, 0, n-1)
    for i in range(n):
        print(arr[i], end=" ")

print("\n")

'''
Time Complexity:
Worst: O(n^2)
Average: O(nlogn)
Important Note: Worst Case occurs when pivot is always the smallest or the
largest element.
'''
