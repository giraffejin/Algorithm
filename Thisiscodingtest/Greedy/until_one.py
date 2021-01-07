#1이 될때까지(chapter3-04)

N,K = map(int,input().split())

count = 0
def solution1(N,K,count):
    while(N>1):
        if(N%K==0):
            N = N//K
        else:
            N-=1

        count += 1
    return count

#solution2
while True:
    target = (N//K)*K
    count += N-target
    N = target
    if(N<K):
        break
    count +=1
    N = N//K

count += (N - 1)
print(count)
print(solution1(N,K,count))

