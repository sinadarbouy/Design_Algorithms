
class Solution:
    def countAndSay(self, n: int) -> str: 
        if n == 1:
          return "1"
        def calcualteRLE(string: str) -> str:
          RLE= []
          i = 0
          while i < len(string):
            count = 1
            while i +1 < len(string) and string[i] == string[i+1]:
              i +=1
              count +=1
            RLE.append(f"{count}{string[i]}")
            i+=1
          return ''.join(RLE)
              
        strRLE="1"
        for _ in range(n-1):
          strRLE = calcualteRLE(strRLE)
        return strRLE 


s = Solution()
print(s.countAndSay(4))
