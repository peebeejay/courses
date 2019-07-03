import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(a, b):
    i = 0
    j = 0
    merged = []
    for x in range(0, len(a) + len(b)):
        if i is len(a):
            merged.append(b[j])
            j += 1
        elif j is len(b):
            merged.append(a[i])
            i += 1
        elif j is len(b) or a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    return merged


print(merge_sort([random.randint(1, 101) for x in range(0, 25)]))
