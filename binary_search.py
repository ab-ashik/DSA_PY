def binary_search_iterative(array, x, low, high):
    
    n = len(array)
    
    while low <= high:
            mid = low + (high - low)//2
    
            if array[mid] == x:
                return mid
            elif x > array[mid]:
                low = mid+1
            else:
                high = mid -1
    

    return -1


def binary_search_recursive(array, x, low, high):
    
    if low <= high:
            mid = low + (high - low)//2
    
            if array[mid] == x:
                return mid
            elif x > array[mid]:
                return binary_search_recursive(array, x, mid+1, high)
            else:
                return binary_search_recursive(array, x, low, mid-1)
    
    else:
        return -1







array = [1, 2, 3, 4, 5, 6, 7, 8]

print(array)

searched_item = int(input("Enter a integer for search: "))

result = binary_search_recursive(array, searched_item, 0, len(array)-1)

if result == -1:
    print("Searched element is not found")
else:
    print("Searched element is found at : ", result)