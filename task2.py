def binary_search(arr, x):
    right_border = len(arr) - 1
    left_border = 0
    iterations = 0
    value = None

    while left_border <= right_border:
        # diap = arr[left_border:right_border + 1]
        iterations = iterations + 1
        mid = (right_border + left_border) // 2
        value = arr[mid]

        if arr[mid] < x:
            left_border = mid + 1
            value = arr[min(left_border, len(arr) - 1)]
        elif arr[mid] > x:
            right_border = mid - 1
        else:
            break

    # if we want to return a near value need to remove the condition and return `value`
    return iterations, value if x <= value else None


array = [0.1, 1, 2, 2.7, 5, 15, 16.2, 17, 18, 18.7, 21, 20, 21, 23.3, 100]
target = 12
res = binary_search(array, target)

print(res)
