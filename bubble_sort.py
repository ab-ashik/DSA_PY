def bubble_sort(list):
    
    for i in range(len(list)) : 
        
        for j in range(len(list)-1) :
            
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
                
    return list

data_list = [15, 8, 11, 5, 9, 19, 2]

print(f"Unsorted List : {data_list}")

sorted_list = bubble_sort(data_list)

print(f"Sorted List : {sorted_list}")
