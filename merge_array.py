from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for the merged array
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]


s = Solution()
nums1 = [2,0,0]
m = 1
nums2 = [1,4]
n = 2
s.merge(nums1,m,nums2,n)
print(nums1)
