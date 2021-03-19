#방 번호 (백준 - 구현 유형)
#https://www.acmicpc.net/problem/1475
#필요한 세트의 개수의 최솟값 구하기

n = list(map(int,input()))
count =[0]*10
for num in n:
    count[num]+=1

if (count[6]+count[9])%2==0:
    num = ((count[6]+count[9])//2)
    count[6],count[9] = num,num
else:
    num = ((count[6] + count[9]) // 2)+1
    count[6],count[9]=num,num

result = max(count)
print(result)



