def quickSort(array, s, e):
    if s < e:
        
        index = partition(array, s, e)
        
        quickSort(array, s, index-1)
        
        quickSort(array, index + 1, e)

def partition(array, l, r):
    
    i = l
    j = r -1
    
    pivot = array[r]
    
    while i < j:
        
        while i < r and array[i] < pivot:
            i = i +1
        while j > l and array[j] > pivot:
            j = j - 1
        
        if i < j:
            array[i], array[j] = array[j], array[i]
        
    if array[i] > pivot:
        array[i], array[r] = array[r], array[i]
        
    return i

arr = [3, 5, 2, 1, 4]
quickSort(arr, 0, len(arr)-1)
print(arr)
        