str = input()
s=str.split()
a=int(s[0])
k=int(s[1])
n=int(s[2])
b=0
check=0
if k>n or a>=n:
    print("-1")
else:
    for i in range(1,k+1):
        if (a+i)%k==0 and (a+i)<=n:
            b=i
            print(i, end= " ")
            check+=1
    if check!=0:
        for i in range(k,n-a+1,k):
            if b+i <= n-a:
                print(b+i, end=' ')
    else:
        print("-1")