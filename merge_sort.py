def merge_sort(a):
    if(len(a) >1  ):
        mid = (len(a))//2
        part_one = merge_sort(a[0:mid])
        part_two = merge_sort(a[mid:])
        return merge(part_one,part_two)
    return a
def merge(part_one,part_two):
    final_list = []
    len_one = len(part_one)
    len_two = len(part_two)
    ind_one = 0
    ind_two = 0
    while(ind_one < len_one and ind_two < len_two):
            if(part_one[ind_one] < part_two[ind_two]):
                final_list.append(part_one[ind_one])
                ind_one += 1
            else:
                final_list.append(part_two[ind_two])
                ind_two += 1
    if(ind_one >= len_one):
        final_list += part_two[ind_two:]
    else:
        final_list += part_one[ind_one:]
        
    return final_list
        
    
print(merge_sort([98]))
