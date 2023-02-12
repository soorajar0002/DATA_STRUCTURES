def merge_sort(array):
    if len(array) > 1:
        m = len(array)//2
        L = array[:m]
        R = array[m:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
       
            
array = [1, 20, 6, 4, 5]
merge_sort(array)
print("Sorted array is: ")
print(array)          
            