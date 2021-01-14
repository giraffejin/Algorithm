#설탕 배달 (백준-그리디 유형)

n = int(input())
result = 0

if n%5==0:
    result = n//5
else:
    a = n//5
    for i in range(a,-1,-1):
        b =n - i*5
        #5kg 봉지로 채우지 못한 부분을 3kg 봉지를 이용하여 채울 수 있는지 확인
        if b%3==0:
            result = i + (b//3)
            break
        else:
            result = -1

print(result)