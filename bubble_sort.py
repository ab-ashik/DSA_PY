def bubble_sort(list):
    
    n = len(list)
    
    for i in range(n) : 
        
        #after first passes if swapped tracker remain false, it mean all items are sorted,
        # unnecessary iteration and comparison is reduced by this
        swapped = False  #swapped tracked added
        
        for j in range(n-i-1) :
            
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
            
        if not swapped:    # same as "if swapped is False"
            break
                
    return list

data_list = [15, 8, 11, 5, 9, 19, 2]

print(f"Unsorted List : {data_list}")

sorted_list = bubble_sort(data_list)

print(f"Sorted List : {sorted_list}")
