#구현 기출 문제- 문자열 재정렬 (chapter12-08)

s = list(input())
#정렬하면 숫자, 문자 순으로 오름차순 정렬
s.sort()

#숫자랑 문자 분리
num = [str(i) for i in range(10)]
num_result = 0
result=''
count = 0 #문자열에서 숫자 포함 여부를 파악

for i in range(len(s)):
    if s[i] in num:
        num_result += int(s[i])
    else:
        result = result+s[i]

#문자열 결과와 숫자 결과 합치기
if count!=0:
    result = str_result+str(num_result)
    
print(result)






