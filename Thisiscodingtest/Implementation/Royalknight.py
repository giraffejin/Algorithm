#왕실의 나이트 문제 (chpater4-02)

dx = [1,-1,1,-1,2,2,-2,-2]
dy = [2,2,-2,-2,1,-1,1,-1]
#steps는 dx,dy 형태로 표현
steps = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

knight = input()
x,y = knight[0],int(knight[1])
char = ['a','b','c','d','e','f','g','h']
x = char.index(x)+1
#x = int(ord(knights[0]))-int(ord('a'))+1


count = 0
for i in range(8):
#for step in steps:
    nx = x + dx[i]
    #nx = x +step[0]
    ny = y + dy[i]
    #ny = y +step[1]
    if(nx>=1 and nx<=8 and ny>=1 and ny<=8):
        count +=1

print(count)