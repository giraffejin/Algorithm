#구현 기출 문제 - 럭키 스트레이트 (chapter12-07)

n = input()
a = (len(n)//2)

#왼쪽 부분과 오른쪽 부분의 합
left = sum(list(map(int,n[0:a])))
right = sum(list(map(int,n[a:])))

#럭키스트레이트 사용 가능 여부 판단
if left==right:
    print('LUCKY')
else:
    print('READY')

