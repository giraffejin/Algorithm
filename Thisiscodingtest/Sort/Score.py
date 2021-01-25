# 이것이 코딩테스트다
# Chapter14-23: 정렬 기출 국영수
# https://www.acmicpc.net/problem/10825

n = int(input())
students=[]
for i in range(n):
    students.append(input().split())

#lambda를 이용해서 배열
students.sort(key= lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

#정렬된 학생의 이름을 출력
for student in students:
    print(student[0])


