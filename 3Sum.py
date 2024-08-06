from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      n = len(nums)
      nums.sort()
      
      result = []
      
      for i in range(n-2):
        if i>0 and nums[i] == nums[i-1]:
          continue
        
        if nums[i] > 0:
            break
        left = i+1
        right = n-1
        while left < right:
          if nums[left]+nums[i]+nums[right] == 0:
            result.append([nums[left],nums[i],nums[right]])
            while left<right and nums[left] == nums[left + 1]:
              left+=1
            while left<right and nums[right] == nums[right-1]:
              right-=1
            left+=1
            right-=1
          elif nums[left]+nums[i]+nums[right] < 0:
            left += 1
          else:
            right -=1
        
      return result

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
