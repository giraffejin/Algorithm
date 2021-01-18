#2007년 (백준 - 구현 유형)

#월과 일 입력
x,y = map(int,input().split())
tone = [1,3,5,7,8,10,12]
tzero = [4,6,9,11]
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
z = 0

#전체 일 수 파악
for i in range(1,x):
    if i in tone:
        z +=31
    elif i in tzero:
        z +=30
    else:
        z+=28

z+=y-1
print(days[z%7])


