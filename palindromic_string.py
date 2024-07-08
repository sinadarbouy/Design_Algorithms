class Solution:
    def longestPalindrome(self, s: str) -> str:
      def checkPalindrome(s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
          left -= 1
          right += 1
        return left+1,right-1
      start,end = 0,0
      for i in range(len(s)):
        # check odd
        left,right = checkPalindrome(s,i,i)
        # check even 
        left2,right2 = checkPalindrome(s,i,i+1)
        
        if right - left > end - start:
          start,end = left,right
        if right2 - left2 > end -start:
          start,end = left2,right2
      
      return s[start:end+1]
              
so = Solution()
s = "cbbd"
print(so.longestPalindrome(s))
