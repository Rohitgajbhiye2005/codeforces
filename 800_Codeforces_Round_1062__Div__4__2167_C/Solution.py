t=int(input())
for _ in range(t):
    odd=0
    even=0
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n):
        if arr[i]%2!=0:
            odd+=1
        else:
            even+=1
    if odd!=0 and even!=0:
        ans=list(sorted(arr))
        print(*ans)
    else:
        print(*arr)
            