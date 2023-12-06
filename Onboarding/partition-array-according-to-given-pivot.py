class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        large=[]
        equal=[]
        for x in range(len(nums)):
            if nums[x]<pivot:
                small.append(nums[x])
            elif nums[x]==pivot:
                equal.append(nums[x])
            elif nums[x]>pivot:
                large.append(nums[x])
        return small+equal+large
