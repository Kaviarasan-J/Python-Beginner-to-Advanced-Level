import pprint


def sort(arr):
    sorted_arr = sorted(arr)
    return  [sorted_arr[0],sorted_arr[-1]]

def find(arr):
    return [min(arr),max(arr)]


def miss(arr,n):
    total = n*(n+1)//1
    arr = sum(arr)
    return total = arr - n

print(miss(arr,2))


arr = [56, 37, 68, 47, 79, 32, 67]
print(sort(arr))
print(find(arr))






