def merge_sort(array):
    
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        
        
        # recursion
        merge_sort(left_array)
        merge_sort(right_array)
        
        # merge
        i = 0    # left array index
        j = 0    # right array index
        k = 0    # merge array index
        
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1

            else:
                array[k] = right_array[j]
                j += 1
                
            k+=1
            
        while i <len(left_array):
            array[k] = left_array[i]
            i+=1
            k+=1
        while j < len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1


array = [2, 3, 5, 1, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(array)
print(array)