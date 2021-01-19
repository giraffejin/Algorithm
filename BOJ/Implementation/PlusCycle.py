#더하기 사이클 (백준 - 구현 유형)
#https://www.acmicpc.net/problem/1110

n = input()
new = ''
result = n
count = 0

while new!=result: #새로 만든 값과 처음의 값이 같아질 때까지
    #한 자리수인 경우 앞에 0붙이기
    if len(n)==1:
        n = '0'+ n

    a = n[1] #주어진 수의 가장 오른쪽 자리 수
    b = (int(n[0])+int(n[1]))%10 #합의 가장 오른쪽 자리 수
    new = str(int(a+str(b)))
    n = new
    count+=1

print(count)
