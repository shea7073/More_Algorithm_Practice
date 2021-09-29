# Implement bubble sort

def bubble(arr):

    for j in range(len(arr)):
        for i in range(len(arr)-1):
            first = arr[i]
            second = arr[i+1]
            if first > second:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp

    print(arr)


bubble([9, 4, 3, 8, 6, 1, 2])