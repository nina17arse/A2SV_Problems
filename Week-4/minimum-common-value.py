class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        minNum=[]
        # l=0
        r=0
        for i in range(len(nums1)):
            while r < len(nums2) and nums1[i] > nums2[r]:
                r+=1

            if r < len(nums2) and nums2[r]==nums1[i] :
                return nums1[i]

        return -1

        

        # return ans 
        