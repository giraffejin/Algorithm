#이것이 코딩테스트다
#Chapter12-12: 구현 기출 기둥과 보 설치 답안 해설
#https://programmers.co.kr/learn/courses/30/lessons/60061

#설치 및 삭제 연산을 요구할때마다 '전체 구조물을 확인하며' 규칙을 확인하는 풀이 방식 적용


#현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x,y,stuff in answer:
        if stuff==0: #설치된 것이 '기둥'인 경우
            #'바닥 위' 또는 '보의 한쪽 끝부분 위' 혹은 다른 기둥 위'라면 정상
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False

        elif stuff==1: #설치된 것이 '보'인 경우
            #한 쪽 끝 부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if[x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False

    return True

def solution(n,build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate==0: #삭제하는 경우
            answer.remove([x,y,stuff]) #일단 삭제
            if not possible(answer): #삭제가 가능한 구조물인지 확인한 후
                answer.append([x,y,stuff]) #가능한 구조물이 아니라면 다시 설치
        if operate==1: #설치하는 경우
            answer.append([x,y,stuff]) #일단 설치
            if not possible(answer): #설치 가능한 구조물인지 확인한 후
                answer.remove([x,y,stuff]) #가능한 구조물이 아니라면 다시 제거

    return sorted(answer)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))

