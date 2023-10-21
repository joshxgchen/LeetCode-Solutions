class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        length = len(nums1) + len(nums2)
        half = length // 2
        #sliding win 2 pointer approach
        
        left = 0
        right = len(nums1)-1 #left
        
        while True:
            mid1 = (left+right) // 2
            mid2 = half - mid1 - 2 #subtract 2 for indexing, off by 1 error and two arrays
            
            Aleft = nums1[mid1] if mid1 >= 0 else float('-inf')
            Aright = nums1[mid1+1] if (mid1 + 1) <len(nums1) else float('inf')
            Bleft = nums2[mid2] if mid2 >= 0 else float('-inf')
            Bright = nums2[mid2+1] if (mid2 + 1) <len(nums2) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright: #we're in the right spot
                #if odd
                if length % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Bright, Aright)) / 2 #cause we want decimal values fam
                
            elif Aleft > Bright:
                right = mid1 - 1
            else:
                left = mid1 + 1
