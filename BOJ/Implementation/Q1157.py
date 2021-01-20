#단어 공부 (백준 - 구현 유형)
#https://www.acmicpc.net/problem/1157
#가장 많이 사용된 알파벳 찾기
#해당 코드의 경우 타임아웃은 발생하지 않으나 수행 시간이 길다

word = input().upper() #단어를 모두 대문자로 변환
a =[0]*26 #알파벳 개수를 세기 위한 리스트. index=0 부터 a를 의미

#각 단어의 횟수 구하기
for char in word:
    i = int(ord(char)) - int(ord('A'))
    a[i]+=1

#가장 큰 값을 가지는 문자 찾기
count = 0 #가장 큰 값을 가지는게 여러개인지 확인
m = max(a)
result_l = [i for i, j in enumerate(a) if j==m] #최대 값을 가지는 인덱스 찾기
if len(result_l)>=2:
    print('?')
else:
    a = result_l[0]+int(ord('A'))
    print(chr(a))







