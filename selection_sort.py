def selection_sort(array):
    
    for i in range(0, len(array)-1):
        
        current_min_index = i
        
        for j in range(i+1, len(array)):
            
            if array[j] < array[current_min_index]:
                current_min_index = j
        
        array[i], array[current_min_index] = array[current_min_index], array[i]
        



array = [2, 6, 5, 1, 3, 4]

selection_sort(array)

print(array)