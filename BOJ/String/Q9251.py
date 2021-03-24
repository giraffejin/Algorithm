# LCS (백준 - 문자열 유형)
# https://www.acmicpc.net/problem/9251
# LCS의 길이 구하기
# 2차원 배열을 활용하는 경우 수행 시간이 오래 걸린다

word1 = input()
word2 = input()
w1,w2 = len(word1),len(word2)

array =[[0]*(w2+1) for _ in range(w1+1)]

for i in range(1,w1+1):
    for j in range(1,w2+1):
        if word1[i-1]==word2[j-1]:
            array[i][j] = array[i-1][j-1]+1
        else:
            array[i][j] = max(array[i-1][j],array[i][j-1])

answer = array[-1][-1]
print(answer)