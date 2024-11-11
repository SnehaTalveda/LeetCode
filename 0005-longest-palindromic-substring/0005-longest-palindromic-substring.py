class Solution:
    def longestPalindrome(self, s: str) -> str:
        st=s[0]
        l=1
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > l and s[i:j+1]==s[i:j+1][::-1]:
                    l=j-i+1
                    st=s[i:j+1]
        return st