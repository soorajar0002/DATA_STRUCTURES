def quick_sort(array,left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort(array, left , pivot-1)
        quick_sort(array, pivot+1, right)

def partition(array, left, right):
    i = left
    j = right-1
    pivot = array[right]
    while i < j:
        while i<right and array[i]<pivot:
            i=i+1
        while j>left and array[j]>pivot:
            j=j-1
        if i<j:
            array[i],array[j]=array[j],array[i]
    if array[i]>pivot:
        array[i],array[right]=array[right],array[i]
    return i 

array = [73,2,13,65,23,1,0]
size = len(array)
quick_sort(array,0,size-1)
print(array)