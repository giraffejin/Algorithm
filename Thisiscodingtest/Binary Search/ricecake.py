#떡볶이 떡 만들기 문제 (chapter7-03)

n,m = map(int,input().split())
a = list(map(int,input().split()))
end = max(a)
start = 0
result = 0
#이진 탐색에 반복문 활용(현재 얻을 수 있는 떡의 양에 따라 자르는 위치를 결정하기 때문에 반복문 활용이 더 나음)
while start<=end:
    cut = 0
    mid = (start+end)//2
    for i in a:
        if i>mid:
            cut += i-mid
    if cut<m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)





