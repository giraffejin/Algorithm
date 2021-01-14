#그리디 기출문제 - 모험가 길드 (chapter11-01)

#모험가의 수와 각 모험가의 공포도 값 입력받기
n = int(input())
fear = list(map(int,input().split()))

#공포도를 오름차순으로 정렬
fear.sort()

#여행을 떠날 수 있는 그룹수
group = 0
#그룹에 속하는 탐험가의 수
count = 0

for i in fear:
    count+=1
    if count>=i:
        group+=1
        count=0

print(group)


