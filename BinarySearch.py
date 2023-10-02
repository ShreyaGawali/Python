#Given a sorted array of size N and an integer K, find the position(0-based indexing)
# at which K is present in the array using binary search.

def binary_search(arr, n, k):
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1

N = 5
arr = [11, 22, 33, 44, 55]
K = 44
result = binary_search(arr, N, K)
if result != -1:
    print(f"Element {K} found at index {result}")
else:
    print(f"Element {K} not found in the array")
