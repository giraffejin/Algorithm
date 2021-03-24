# LCS (백준 - 문자열 유형)
# https://www.acmicpc.net/problem/9251
# LCS의 길이 구하기
# DP를 활용하면 수행 시간이 훨씬 단축됨

word1 = input()
word2 = input()
w1,w2 = len(word1),len(word2)
dp =[0]*1000 #dp테이블 초기화

for i in range(w1):
    max_dp = 0
    for j in range(w2):
        if max_dp <dp[j]:
            max_dp = dp[j]
        elif word1[i]==word2[j]:
            dp[j] = max_dp+1

print(max(dp))