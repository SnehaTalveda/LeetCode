class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        res=math.gcd(mi,ma)
        return res