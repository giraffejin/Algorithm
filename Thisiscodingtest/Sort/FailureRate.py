# 이것이 코딩테스트다
# Chapter14-25: 정렬 기출 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N,stages):
    answer=[]
    users = len(stages)

    #실패율 계산
    for i in range(1,N+1):
        stage_user = stages.count(i)
        if users==0:
            fail_rate=0
        else:
            fail_rate = stage_user/users
        answer.append((i,fail_rate))
        users-=stage_user

    #실패율  정렬
    answer.sort(key=lambda x:x[1], reverse=True)
    #스테이지 번호 출력
    answer=[i[0] for i in answer]
    return answer

stages = [2,1,2,6,2,4,3,3]
N = 5
print(solution(N,stages))
