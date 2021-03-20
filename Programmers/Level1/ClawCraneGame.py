# 프로그래머스 Level 1
# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형 뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061


board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves =[1,5,3,5,1,2,1,4]

def solution(board,moves):
    bucket=[] #뽑은 인형을 넣을 바구니
    answer =0
    #인형을 뽑기 위한 크레인을 이동
    for move in moves:
        for i in range(len(board)): #뽑을 인형이 있을 때까지 이동
            doll = board[i][move-1]
            if doll!=0: #뽑을 인형이 있으면
                board[i][move-1]=0 #인형 없음 처리
                bucket.append(doll) #바구니에 인형을 넣기
                break
            else: #뽑을 것 없으면 그냥 진행
                continue
        #바구니에 담긴 것이 동일한 것이 있는지 확인
        bucket_len = len(bucket)
        if bucket_len>1: #바구니에 2개이상 담기면
            if bucket[bucket_len-1]==bucket[bucket_len-2]: #서로 동일한 인형이면
                bucket.pop() #위에 2개 삭제
                bucket.pop()
                answer+=2


    return answer

print(solution(board,moves))