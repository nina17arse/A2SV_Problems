class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        ans=True
        m1=arr.index(max(arr))
        if n < 3:
            return False
        elif m1==0 or m1==n-1:
            return False
        else:
            for i in range(0,m1):
                if arr[i] >= arr[i+1]:
                    ans=False
            for u in range(m1,n-1):
                if arr[u] <= arr[u+1]:
                    ans=False
                
            return ans

            

            

                
            



        