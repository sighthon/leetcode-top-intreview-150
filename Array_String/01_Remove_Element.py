# https://leetcode.com/problems/remove-element
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    # pointer from start cares about val and pointer from
    # end cares about non val
    idx = 0
    jdx = len(nums) - 1

    while idx <= jdx and idx < len(nums) and jdx >= 0:
        while idx < len(nums) and nums[idx] != val:
            idx += 1
        while jdx >= 0 and nums[jdx] == val:
            jdx -= 1

        if idx <= jdx and idx < len(nums) and jdx >= 0:
            # print(idx, jdx)
            nums[idx], nums[jdx] = nums[jdx], nums[idx]
            idx += 1
            jdx -= 1

    # print(idx, jdx)
    return jdx + 1
