n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(len(arr)):
    if(arr[i]%2==0):
        k.append(arr[i])
print(k[-1]) 