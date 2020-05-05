#First element as pivot
#When Pivot is first element
def quick_sort(a,p,r):
    if(p < r):
        q = partition(a,p,r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)

def partition(a,p,r):
    pivot  = p
    pivot_element = a[p]
    '''change was to select left as p because p-1 will come to p after first increment'''
    left = p
    '''Change range from first element after p to last element'''
    for right in range(p+1,r):
        if(a[right] <= pivot_element):
            left += 1
            a[left],a[right] = a[right],a[left]
    '''Do not increment the left as we have element grater than pivot on right of left
    Doing this will put alement greater than pivot on left side which is not desired'''
    a[left],a[pivot] = a[pivot],a[left]
    return left

input = [12,45,65,34,2,39,900,894,1800]
quick_sort(input, 0, len(input)-1)
print(input)
