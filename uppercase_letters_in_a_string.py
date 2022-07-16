str=input()
count=0
m='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(str)):
    for j in range(len(m)):
        if(str[i]==m[j]):
            count+=1
print(count)
