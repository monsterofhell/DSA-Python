'''First element as pivot'''
def quick_sort(a,p,r):
    if(p < r):
        q = partition(a,p,r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)

def partition(a,p,r):
    pivot  = r
    pivot_element = a[r]
    left = p-1
    for right in range(p,r):
        if(a[right] <= pivot_element):
            left += 1
            a[left],a[right] = a[right],a[left]
    a[left+1],a[pivot] = a[pivot],a[left + 1]
    return left+1

input = [12,45,65,34,2,39,900,894,1800]
quick_sort(input, 0, len(input)-1)
print(input)
