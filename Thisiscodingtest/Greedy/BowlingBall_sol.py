#그리디 기출 문제 - 볼링공 고르기(chapter11-05) 답안 해설
n,m = map(int,input().split())
data = list(map(int,input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in data:
    #각 무게에 해당하는 볼링공의 개수 count
    array[x]+=1

result = 0
#1부터 m까지의 각 무게에 대하여 처리
for i in range(1,m+1):
    n-= array[i] #무게가 i인 볼링공의 개수 제외
    result += n*array[i] #B가 선택하는 경우의 수와 곱하기

print(result)


