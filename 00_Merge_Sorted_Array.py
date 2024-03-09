# https://leetcode.com/problems/merge-sorted-array
from typing import List


# O(m*n)
# Requires O(n) iteration over nums2 to fit the replaced element from nums1
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    idx = 0
    while idx < m and n > 0:
        if nums1[idx] <= nums2[0]:
            idx += 1
            continue

        temp = nums1[idx]
        nums1[idx] = nums2[0]
        jdx = 1
        while jdx < n and nums2[jdx] < temp:
            nums2[jdx - 1] = nums2[jdx]
            jdx += 1
        nums2[jdx - 1] = temp

    # individual iteration on nums2
    jdx = 0
    while jdx < n:
        nums1[m + jdx] = nums2[jdx]
        jdx += 1


# O(m+n)
# Start iterating over both arrays from back and replacing 0's at the end of nums1
def mergeFromTheEnd(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # update and replace nums2 first element
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        print(nums1)
        print(nums2)

    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        m -= 1
        n -= 1
