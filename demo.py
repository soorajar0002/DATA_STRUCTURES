def max_heapify(array,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and array[largest] < array[left]:
        largest = left
        
    if right < n and array[largest] > array[right]:
        largest = right
    
    if largest!=i:
        array[i],array[largest]=array[largest],array[i]
        max_heapify(array,n,largest)
        
array = [4,32,1,3,43,2,64]
n = len(array)
for i in range(n//2-1,-1,-1):
    max_heapify(array,n,i)
print("MAX HEAP")
for i in range(n):
    print(array[i])
    