import random
from collections import defaultdict

comps = {}
comps = defaultdict(lambda: [], comps)

# Challenge Question 1.5

def greatest(arr):
    if len(arr) <= 1:
        return arr[0]
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return compare(greatest(left), greatest(right))

def compare(a, b):
    if a > b:
        comps[a].append(b)
        return a
    else:
        comps[b].append(a)
        return b

def second_greatest(arr):
    greatest_num = greatest(arr)
    # runtime of max function below is log2(n)-1 instead of n,
    # which makes it acceptable to use
    return max(comps[greatest_num])

# Runtime calculation for greatest:
# =sigma(2^l, 0, log2(n)-1)
# =2^(log2(n)-1 = n-1
#
# Runtime calculation for max:
# =[log2(n)-1]
#
# Add them together:
# =[(n-1)+(log2(n)-1)]
# =[n+log2(n)-2], which meets the requirement ✅
print(second_greatest([1, 2, 3, 4, 5, 6, 7, 8]))
