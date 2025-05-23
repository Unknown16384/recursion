def binary_search_recursive(array, target):
    def bsr(arr, low, high, key):
        if high > low:
            mid = (high + low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return bsr(arr, low, mid-1, key)
            else:
                return bsr(arr, mid+1, high, key)
        return -1
    return bsr(array, 0, len(array), target)
