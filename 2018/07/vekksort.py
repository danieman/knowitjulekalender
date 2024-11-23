# Longest Increasing Subsequence lis() implementert i O(n * log(n))
# Longest Non-Decreasing Subsequence lnds() (treg)
# LNDS fra Wikipedia lnds_wiki() (rask)

from math import ceil

def bin_search(arr, left, right, key):
    while right > left + 1:
        mid = left + (right - left)//2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid
    return right

def lis(arr):
    ends = [0 for i in arr]
    ends[0] = arr[0]
    cur_idx = 1
    for i in range(1, len(arr)):
        if arr[i] < ends[0]:
            ends[0] = arr[i]
        elif arr[i] > ends[cur_idx-1]:
            ends[cur_idx] = arr[i]
            cur_idx += 1
        else:
            new_idx = bin_search(ends, -1, cur_idx-1, arr[i])
            ends[new_idx] = arr[i]
    return cur_idx

def lnds(arr):
    ends = [0 for i in arr]
    ends[0] = arr[0]
    cur_idx = 1
    for i in range(1, len(arr)):
        if arr[i] < ends[0]:
            ends[0] = arr[i]
        elif arr[i] >= ends[cur_idx-1]:
            ends[cur_idx] = arr[i]
            cur_idx += 1
        else:
            new_idx = bin_search(ends, -1, cur_idx-1, arr[i])
            if arr[i] in ends[:cur_idx]:
                ends[new_idx+1] = arr[i]
            ends[new_idx] = arr[i]
    return cur_idx

def lnds_wiki(seq):
    N = len(seq)
    M = [None] * N
    L = 0
    for i in range(1, N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = ceil((lo+hi)/2.0)
            if seq[M[mid]] <= seq[i]:
                lo = mid+1
            else:
                hi = mid-1
        newL = lo
        M[newL] = i
        if newL > L:
            L = newL
    return L

nums = [int(n.strip()) for n in open('input.txt')]
print(lnds_wiki(nums))