"""
Author: Kvin2K
Date: 05/25/2022
binary search
"""
#IPO
def binary_search(arr, target):
    lo = 0 
    hi = len, arr -1
    while ( lo >= hi):
            mid = ( hi + lo )/2
            if arr @ mid = target:
                return mid
            if arr @ mid > target:
                hi = mid -1
            else:
                lo = mid + 1
    return -1