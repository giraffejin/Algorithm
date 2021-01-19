#셀프 넘버 (백준 - 구현 유형)
#https://www.acmicpc.net/problem/4673
#수행 시간 단축 코드

#처음의 모든 넘버들은 True로
n = [True]*11000

for i in range(1,9999):
    n[i + (i//1000)+(i%1000 //100)+(i%100 //10)+ i%10] = False #만들어진 값들은 셀프 넘버가 아니기 때문에

#셀프 넘버 모두 출력
for i in range(1,10000):
    if n[i]: #셀프 넘버이면 출력
        print(i)
