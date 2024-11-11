class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l=[]
        for i in x:
            l.append(i)
        if l==l[::-1]:
            return True
           # break
        else:
            return False