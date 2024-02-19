t=int(input())
for _ in range(t):
    n=int(input())
    str=input()
    nums=list(map(int,str))
    # print(nums)
    d={0:1}
    prefNum=0
    res=0
    
    for i in range(n):
        prefNum += (nums[i])
    
        x = prefNum - i - 1
        if x not in d:
            d[x] = 0
        d[x] += 1
        res += d[x] - 1
        
    print(res)