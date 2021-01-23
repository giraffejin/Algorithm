# 이것이 코딩테스트다
# Chapter12-19: DFS/BFS 기출 연산자 끼워 넣기
#https://www.acmicpc.net/problem/14888

#itertools 라이브러리를 통해 가능한 모든 순열을 만들고 집합을 활용해 중복되는 순열을 제거
#시간초과는 발생하지 않으나 수행시간이 오래 걸린다

from itertools import permutations
n = int(input())
a = list(map(int,input().split()))
op = list(map(int,input().split()))

operator =''
op1 = ['+','-','*','/']
#가능한 연산식을 만들기 위해 연산자 변환
for i in range(len(op)):
    operator+=op[i]*op1[i]

operator = list(operator)

#가능한 연산자 순열 생성 -> 집합을 활용하여 중복되는 경우 제거
candidates = list(permutations(operator,n-1))
candidates = list(set(candidates))


#연산식 수행
def calculate(a,b,op):
    if op=='-':
        result = a-b
    elif op=='+':
        result = a+b
    elif op=='*':
        result = a*b
    else:
        if a*b<0: #서로 부호가 다른 경우
            result =-1*(abs(a)//abs(b))
        else:
            result = a // b
    return result

#전체 가능한 경우의 수에 대해 계산
results =[]
for candidate in candidates:
    result = a[0]
    for i in range(n-1):
        result = calculate(result,a[i+1],candidate[i])
    results.append(result)

print(max(results))
print(min(results))

