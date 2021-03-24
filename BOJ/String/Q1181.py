# 단어정렬 (백준 - 문자열 유형)
# https://www.acmicpc.net/problem/1181
# 길이가 짧고 사전순으로 배열

import sys
n = int(input())
words =[]

for i in range(n):
    word = sys.stdin.readline().rstrip()
    words.append((word,len(word)))

#동일 단어 제거
words = list(set(words))

#조건에 따라 정렬
answers = sorted(words,key=lambda words:(words[1],words[0]))

#정렬된 단어 출력
for answer in answers:
    print(answer[0])



