#부품 찾기 문제 (chapter7-02)

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if(array[mid]==target):
        return mid
    elif(array[mid]>target):
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

for i in range(m):
    result = binary_search(a,b[i],0,n-1)
    if result == None:
        print("no", end= ' ')
    else:
        print("yes", end=' ')