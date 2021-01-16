#그리디 기출 문제 - 무지의 먹방 라이브 (chapter11-06)
#아래의 풀이는 입력값이 커지는 경우 시간 초과가 발생
#책에서 제공하는 테스트 데이터 값에 대해서는 올바른 값 출력

food_times =[3,1,2]
k = 5

def solution(food_times,k):
    i = 0  # 시간을 재기 위한 요소
    type = 0  # 음식 종류를 나타내기 위한 변수
    while i<=k:
        if sum(food_times)==0: #모든 음식을 다 먹었으면 -1을 반환
            answer = -1
        if food_times[type]>0: #남아있는 음식이 있다면
            food_times[type]-=1 #해당 음식을 먹고
            answer = type+1 #다음 차례에 먹을 음식
            i+=1 #시간을 하나 증가

        type = (type+1)%len(food_times) #다음 번에 볼 음식

    return answer

print(solution(food_times,k))