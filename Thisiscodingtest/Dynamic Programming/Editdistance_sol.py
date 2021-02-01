# 이것이 코딩테스트다
# Chapter16-36: 다이나믹 프로그래밍 기출 편집 거리 답안 해설
# LCS를 활용하려고 하였으나 가능한 연산 중 교체에 해당하는 것을 처리할 수 없음
# (i,j)를 기준으로 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당


#최소 편집 거리(Edit Distance) 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1,str2):
    n = len(str1)
    m = len(str2)

    #다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp=[[0]* (m+1) for _ in range(n+1)]

    #DP테이블 초기 설정
    for i in range(1,n+1):
        dp[i][0] = i
    for j in range(1,m+1):
        dp[0][j]=j

    #최소 편집 거리 계산
    for i in range(1,n+1):
        for j in range(1,m+1):
            #문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i-1]==str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                #문자가 다르다면 3가지 경우(삽입, 삭제, 교체) 중에서 최솟값 찾기
                dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1])

    return dp[n][m]

#두 문자열을 입력 받기
str1 = input()
str2 = input()

#최소 편집 거리 출력
print(edit_dist(str1,str2))
