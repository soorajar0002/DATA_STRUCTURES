def selection_sort(list1):
    for i in range(len(list1)):
        min = i
        for j in range(i+1, len(list1)):
            if list1[j]<list1[min]:
                min = j
        
        list1[i],list1[min]=list1[min],list1[i]
        print(list1)
        
list1 = [44,32,1,4,22,34]
selection_sort(list1)
print(list1)
  
