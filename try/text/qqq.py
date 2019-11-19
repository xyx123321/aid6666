class Solution:
    a=0
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(str)):
            for j in range(i,len(str)):
                if i==j:
                    if self.huiwen(str[i,j+1]):

    def huiwen(self, l):
        for i in range(len(l)//2):
           if l[i]!=l[-i-1]:
               return False
        return len(l)