#구현 기출 문제 - 문자열 압축 (chapter12-09)

def solution(s):
    max_len = len(s)//2 #묶을 수 있는 최대 단위
    answers =[] #각 단위 별 결과 값
    for i in range(1,max_len+1): #최대 묶을 수 있는 단위까지 완전 탐색
        result =""
        first = s[0:i] #처음에 묶이는 단위
        count = 1 #동일한 단위가 나온 횟수
        for j in range(i,len(s),i): #i부터 문자열의 끝까지 단위 i씩 뛰기
            if first == s[j:j+i]:
                count+=1
            else:
                if count>1:
                    result += str(count)+first
                else:
                    result += first
                first = s[j:j+i]
                count = 1

        if count>1:
            result += str(count)+first
        else:
            result += first
        answers.append(len(result))

    answer = min(answers)
    return answer




