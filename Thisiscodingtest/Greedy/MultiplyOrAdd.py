#그리디 기출문제 - 곱하기 혹은 더하기 (chapter11-02)

#문자열 S는 띄어쓰기 없이 문자열로 받기
s = input()

# 결과값 초기화
result = int(s[0])

#문자열의 값을 하나씩 읽어나가며 값 구하기
for i in range(len(s)):
    num = int(s[i])
    #0과 1이 아닌 모든 경우에 대해서는 곱하기의 값이 더 크다
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)