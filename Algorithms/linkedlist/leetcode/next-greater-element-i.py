class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        stack=[]
        dic={}
        x=None
        for i in range(len(nums1)):
            dic[nums1[i]]=-1
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                x=stack.pop()
                if x in dic:
                    dic[x]=nums2[i] 

            stack.append(nums2[i])
        # print(dic.values())
                

        return dic.values()