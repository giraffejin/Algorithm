# 이것이 코딩테스트다
# Chapter15-27: 이진 탐색 기출 정렬된 배열에서 특정 수의 개수 구하기 답안 해설

# 이진 탐색 함수를 2개 작성하여 문제를 해결하는 풀이
# first 함수는 데이터가 존재할 때 가장 첫번재 위치를 찾는 이진 탐색 함수
# last 함수는 데이터가 존재할 때 가장 마지막 위치를 찾는 이진 탐색 함수

#정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array,x):
    n = len(array) #데이터의 개수
    #x가 처음 등장한 인덱스 계산
    a = first(array,x,0,n-1)
    #수열에 x가 존재하지 않는 경우
    if a==None:
        return 0 #값이 x인 원소의 개수는 0개이므로 0 반환
    #x가 마지막으로 등장한 인덱스 계산
    b = last(array,x,0,n-1)

    #개수를 반환
    return b-a+1

#처음 위치를 찾는 메서드
def first(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if(mid==0 or target>array[mid-1]) and array[mid]==target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid]>=target:
        return first(array,target,start,mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우
    else:
        return first(array,target,mid+1,end)
    
#마지막 위치를 찾는 메서드
def last(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    #해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if(mid==0 or target<array[mid+1]) and array[mid]==target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid]>target:
        return last(array,target,start,mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우
    else:
        return last(array,target,mid+1,end)

n,x = map(int,input().split())
array = list(map(int,input().split()))

#값이 x인 데이터의 개수 계산
count = count_by_value(array,x)

#값이 x인 원소가 존재하지 않는다면
if count==0:
    print(-1)
else:
    print(count)