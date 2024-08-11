from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
      anagrams = {}

      for s in strs:
          sorted_str = ''.join(sorted(s))
          
          if sorted_str not in anagrams:
              anagrams[sorted_str] = []
          
          anagrams[sorted_str].append(s)

      return list(anagrams.values())
    
    def groupAnagramsWithoutSortfunction(self, strs: List[str]) -> List[List[str]]:
      anagrams = {}

      for s in strs:
          # Use a fixed-size list for character frequency counts
          count = [0] * 26
          for char in s:
            count[ord(char) - ord('a')] += 1
          
          # Use the tuple of counts as the key
          key = tuple(count)
          if key not in anagrams:
            anagrams[key] = []
          anagrams[key].append(s)

      return list(anagrams.values())
        
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]
print(s.groupAnagramsWithoutSortfunction(strs))
