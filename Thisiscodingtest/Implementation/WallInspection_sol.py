#이것이 코딩테스트다
#Chapter12-14: 구현 기출 외벽 점검 답안 해설
#https://programmers.co.kr/learn/courses/30/lessons/60062

#친구를 나열하는 모든 경우의 수를 각각 확인하는 완전 탐색을 활용
#원형 나열된 데이터의 경우 길이를 2배로 늘려서 원형을 일자 형태로 변환하여 활용

from itertools import permutations
def solution(n,weak,dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1 #투입할 친구의 최솟값을 찾아야 하므로

    #취약점의 위치를 각각 시작점으로 설정
    for start in range(length):
        for friends in list(permutations(dist,len(dist))): #친구를 모두 나열하는 모든 경우의 수에 대하여
            count=1 #투입할 친구의 수
            #해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start]+friends[count-1]

            #시작점부터 모든 취약지점을 확인
            for index in range(start,start+length):
                #점검할 수 있는 위치를 벗어난 경우
                if position <weak[index]:
                    count+=1 #친구를 투입
                    if count>len(dist): #친구를 최대로 투입한 경우
                        break
                    position = weak[index]+friends[count-1]
            answer = min(answer,count) #최솟값 계산

    if answer >len(dist):
        return -1
    return answer
