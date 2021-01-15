#그리디 기출 문제- 문자열 뒤집기 (chapter11-03)

s = input()
count =[0,0]

#0과 1이 각각 연속적으로 나온 횟수 비교
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count[int(s[i])] +=1

#마지막 값은 연속 횟수에 추가
count[int(s[len(s)-1])] +=1

#연속적으로 나온 횟수가 적은 수를 뒤집어 주면 최소의 횟수로 모두 동일하게 만들 수 있음
result = min(count[0],count[1])
print(result)