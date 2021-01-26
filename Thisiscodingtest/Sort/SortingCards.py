# 이것이 코딩테스트다
# Chapter14-26: 정렬 기출 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq
import sys
input = sys.stdin.readline
n = int(input())

#카드 묶음의 크기
cards=[]
for i in range(n):
    heapq.heappush(cards,int(input()))

result = 0
while len(cards)!=1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    new_card = card1+card2
    heapq.heappush(cards,new_card)
    result += new_card

#마지막 묶음을 더해주기
print(result)