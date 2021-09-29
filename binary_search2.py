# Implement binary search without looking at previous solutions

def recursive(arr, num):

    first = 0
    last = len(arr)-1
    mid = (first + last) // 2
    if first > last:
        return False
    else:
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            return recursive(arr[mid+1:], num)
        elif arr[mid] > num:
            return recursive(arr[0:mid], num)



print(recursive([1, 2, 4, 5, 6, 9], 5))