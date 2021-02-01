# 이것이 코딩테스트다
# Chapter16-35: 다이나믹 프로그래밍 기출 못생긴 수 답안 해설
# 못생긴 수에 2,3,5를 곱한 수 또한 못생긴 수에 해당
# 각 배수를 곱한 수를 못생긴 수가 되도록 해준다

n = int(input())
d=[0]*(n)
d[0]=1 #첫번째 못생긴 수는 1
i2,i3,i5 = 0,0,0
mul2, mul3, mul5 = 2,3,5 #초기에 곱할 값

#1부터 n까지 못생긴 수를 찾기
for i in range(1,n):
    next = min(mul2,mul3,mul5)
    d[i] = next

    if next==mul2:
        i2+=1
        mul2 = d[i2]*2

    if next==mul3:
        i3+=1
        mul3 = d[i3]*3

    if next==mul5:
        i5+=1
        mul5 = d[i5]*5

print(d[n-1])





