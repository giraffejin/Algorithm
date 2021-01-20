#단어 공부 (백준 - 구현 유형) 답안 해설
#https://www.acmicpc.net/problem/1157
#해당 코드를 사용하면 수행 시간 단축이 가능하다
#대문자가 가지는 ASCI 코드 범위를 활용하고 문자열에서 해당 문자의 개수를 파악하기 위해 count 내장함수 활용

word = input().upper() #단어를 모두 대문자로 변환
result_l = [word.count(chr(c)) for c in range(65,91)] #단어의 문자 수 세기
m = max(result_l)

if result_l.count(m)==1: #최대 값을 가지는 인덱스가 1개인 경우
    print(chr(result_l.index(m)+65)) #문자로 변환
else:
    print('?')