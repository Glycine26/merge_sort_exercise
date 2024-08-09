from pprint import pprint
def merge_sort(elements,key,descending):
    n = len(elements)
    if n <=1:
        return elements
    mid = n//2
    left = elements[:mid]
    right = elements[mid:]
    
    merge_sort(left,key,descending)
    merge_sort(right,key,descending)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if descending is True:
            if left[i][key] <= right[j][key]:
                elements[k] = right[j]
                j+=1
            else:
                elements[k] = left[i]
                i+=1
            k+=1
        else:
            if left[i][key] <= right[j][key]:
                elements[k] = left[i]
                i+=1
            else:
                elements[k] = right[j]
                j+=1
            k+=1

            #     elements[k] = left[i]
            #     i+=1
            # else:
            #     elements[k] = right[j]
            #     j+=1
            #     k+=1
    while i < len(left):
        elements[k] = left[i]
        i+=1
        k+=1
        
    while j < len(right):
        elements[k] = right[j]
        j+=1
        k+=1
            

elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
result = merge_sort(elements,key="name",descending=True)
pprint(elements)