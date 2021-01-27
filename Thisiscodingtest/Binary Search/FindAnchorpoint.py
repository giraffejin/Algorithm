# 이것이 코딩테스트다
# Chapter15-28: 이진 탐색 기출 고정점 찾기

n = int(input())
array = list(map(int,input().split()))

def binary_search(array,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == mid: #인덱스와 해당 값이 동일한 원소: 고정점
        return mid
    elif array[mid]<mid: #인덱스가 해당 값보다 큰 경우 오른쪽 확인
        return binary_search(array,mid+1,end)
    else: #인덱스가 해당 값보다 작은 경우 왼쪽 확인
        return binary_search(array,start,mid-1)

result = binary_search(array,0,n-1)

if result==None:
    print(-1)
else:
    print(result)
