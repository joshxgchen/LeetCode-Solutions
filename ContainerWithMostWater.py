class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        left = 0 
        right = len(height)-1
        
        prod = 0
        while left<right:
            multiplier = min(height[left], height[right])
            prod = max(prod, multiplier*(right-left))
            if height[left] < height[right]: #add case for oob
                left+=1
            else:
                right-=1
        return prod
        
