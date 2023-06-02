#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return  
            
    def selectionSort(self, arr,n):
        for x in range(n):
            min=x
            for j in range(x+1,n):
                if arr[j]<arr[min]:
                    min=j
            (arr[x],arr[min])=(arr[min],arr[x])
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
