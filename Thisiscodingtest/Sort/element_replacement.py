#두 배열의 원소 교체(chapter6-04)

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

i=0
while i<=k-1:
#for i in range(k):
    if(a[i]<b[i]):
        a[i],b[i] = b[i],a[i]
        i+=1
        
    else:
        break

print(sum(a))
