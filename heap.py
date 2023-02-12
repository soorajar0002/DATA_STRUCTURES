def max_heapify(Arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*1+2
    
    if left < n and Arr[largest] < Arr[left]:
        largest = left

    if right < n  and Arr[largest] < Arr[right]:
        largest = right

    if largest!=i:
        Arr[i],Arr[largest]=Arr[largest],Arr[i]
        max_heapify(Arr,n, largest) 
            
Arr = [2,66,30,5,9,10] 
n = len(Arr)
for i in range(n//2-1,-1,-1):
    max_heapify(Arr,n,i)

print("MAX HEAP IS")
for i in range(n):
    print(Arr[i])