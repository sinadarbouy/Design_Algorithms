from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
      first_min  = second_min = float("inf")
      for i in range(len(nums)):
        if nums[i]<=first_min:
          first_min=nums[i]
        elif nums[i]<= second_min:
          second_min=nums[i]
        else:
          return True
      return False

s =Solution()
print(s.increasingTriplet([20,100,10,12,5,13]))
