# 프로그래머스 Level 1
# 월간 코드 챌린지 시즌1
# 두개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    cases = list(combinations(numbers, 2))
    answer = []

    # 더할 수 있는 모든 수를 구하기
    for case in cases:
        answer.append(case[0] + case[1])

    # 중복 경우의 수 제거
    answer = list(set(answer))
    answer.sort()
    return answer

numbers=[5,0,2,7]
print(solution(numbers))


