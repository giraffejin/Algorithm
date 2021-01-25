# 이것이 코딩테스트다
# Chapter14-24: 정렬 기출 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
home = list(map(int,input().split()))
home.sort() #집의 번호를 오름차순으로 정렬

#중앙에 위치하는 집에 안테나를 설치해야 함
mid = (len(home)-1)//2
print(home[mid])
