#소트인사이드 (백준 - 문자열 유형)
#https://www.acmicpc.net/problem/1427
#자리수를 내림차순으로 정렬하여 출력

#정렬하고자 하는 수 N을 입력 받기
n = list(input())
n.sort(reverse=True)

#문자열로 변환하기
answer = "".join(n)
print(answer)

