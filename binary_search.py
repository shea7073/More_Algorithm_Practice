# Iterative and recurisve versions of binary search

def iterative(arr, num):

    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:

        mid = (first + last) // 2

        if arr[mid] == num:
            found = True
        else:
            if num < arr[mid]:
                last = mid-1
            else:
                first = mid + 1
    return found


#print(iterative([1, 2, 3, 4, 5], 5))


def recursive(arr, num):

    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2

        if arr[mid] == num:
            return True
        else:
            if num > arr[mid]:
                return recursive(arr[mid+1:], num)
            if num < arr[mid]:
                return recursive(arr[0:mid], num)


print(recursive([1, 2, 3, 4, 5, 6], 9))