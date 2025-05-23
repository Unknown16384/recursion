def sum_list(arr):
    if len(arr) > 0:
        return arr[0] + sum_list(arr[1:])
    else:
        return 0
