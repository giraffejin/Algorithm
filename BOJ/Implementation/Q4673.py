#셀프 넘버 (백준 - 구현 유형)
#https://www.acmicpc.net/problem/4673

nonself =[]
#완전 탐색을 활용해 전체 경우의 수 파악
for i in range(1,10000):
    a= i%1000
    b = i%100
    c = i%10
    di = i + (i//1000)+(a//100)+(b//10)+c
    #만들어진 숫자는 i라는 생성자를 갖는 수
    nonself.append(di)

#전체를 돌면서 10000보다 작거나 같은 수 중 di에 속하지 않는 수를 출력
for j in range(10000):
    if j not in nonself:
        print(j)
