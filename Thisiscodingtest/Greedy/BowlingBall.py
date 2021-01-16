#그리디 기출 문제 - 볼링공 고르기 (chapter11-05)

from itertools import combinations
#볼링공의 개수와 공의 최대 무게
n,m = map(int,input().split())
k = list(map(int,input().split()))

#무게에 따른 공의 개수 리스트
weight=[0]*(m+1)
for i in range(n):
    weight[k[i]]+=1

#중복을 고려하지 않는 전체 조합의 개수
full = list(combinations(k,2)) #2개를 뽑는 모든 조합 구하기
a = len(full)
b=0

#중복이 발생하는 조합의 개수
for i in range(len(weight)):
    if weight[i]>1:
        case = [0]*weight[i]
        same = list(combinations(case,2))
        b += len(same)

#전체 가능한 볼링공 번호의 조합 수
result = a-b
print(result)


