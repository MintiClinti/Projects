def binary_search(arr, num):
    print('Entering binary_search')
    lo = 0
    hi = len(arr) - 1


    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            lo = mid + 1
        else:
            hi = mid - 1
    print('Ending binary_search')
    return -1


print(binary_search([1, 2, 3, 4, 5], 5))
