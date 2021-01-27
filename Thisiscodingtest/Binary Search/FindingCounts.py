# 이것이 코딩테스트다
# Chapter15-27: 이진 탐색 기출 정렬된 배열에서 특정 수의 개수 구하기

# 파이썬의 이진 탐색 라이브러리 bisect를 활용한 풀이

from bisect import bisect_left,bisect_right
n,x = map(int,input().split())
array = list(map(int,input().split()))

#left_value와 right_value에 속하는 갯수 찾기
def count_bisect(array,left_value,right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_right(array,right_value)
    return right_index - left_index

if count_bisect(array,x,x)!=0:
    print(count_bisect(array,x,x))
else: #값이 x인 원소가 하나도 없다면 -1
    print(-1)