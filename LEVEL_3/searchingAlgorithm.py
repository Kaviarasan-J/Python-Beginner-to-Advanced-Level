class SearchingAlgorithm:
    def BinarySearch(self, arr, t):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == t:
                return m
            elif arr[m] < t:
                l = m + 1
            else:
                r = m - 1
        return -1

    def LinearSearch(self, arr, t):
        for i in range(len(arr)):
            if arr[i] == t:
                print(i)
                break
        else:
            print("X not found")

# Example usage
arr = [90, 56, 34, 23, 93, 76]
t = 23

# Note: Binary search requires a sorted array
arr_sorted = sorted(arr)  # Sort the array for binary search
b = SearchingAlgorithm()
binary_result = b.BinarySearch(arr_sorted, t)
if binary_result != -1:
    print(f"Binary Search: Element found at index {binary_result} in sorted array.")
else:
    print("Binary Search: Element not found.")

b.LinearSearch(arr, t)  # Linear search can be performed on unsorted array