def linear_search(array, key):
    
    for i in range(0, len(array)):
        if array[i] == key:
            return i
    return -1

array = [1, 2, 3, 4, 5 ,6, 7, 8, 9]
print("Array: ", array)
search_for = int(input("Enter the element you want to search: "))
result = linear_search(array, search_for)

if result == -1:
    print("Searched Value not found")
else:
    print("Searched value is found. It is at index : ", result)