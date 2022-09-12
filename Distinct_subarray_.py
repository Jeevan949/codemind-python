l=int(input())
r=int(input())
count=0
for i in range(l,r+1):
    for j in range(l,r+1):
        if i%2!=0:
            count+=1
            break
        if (i+j)%2!=0:
            count+=1
print(count)