class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valpar(s='',l=0,r=0):
            if len(s)== 2*n:
                res.append(s)
                return
            if l<n:
                valpar(s+'(',l+1,r)
            if r<l:
                valpar(s+')',l,r+1)
        res=[]
        valpar()
        return res