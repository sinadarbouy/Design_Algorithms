
class Solution:
    def countAndSay(self, n: int) -> str:
        strRLE="1"
        if n == 1:
          return strRLE
        for _ in range(n-1):
          strRLE = self.calcualteRLE(strRLE)
        return strRLE 
    def calcualteRLE(self,char: str) -> str:
        RLE= ""
        build = ""
        for i in range(0, len(char)):
            if i != len(char)-1 and char[i] == char[i+1]:
                build += char[i]
            else:
                RLE+= str(len(build)+1) + char[i]
                build = ""
        return RLE

s = Solution()
print(s.countAndSay(4))
