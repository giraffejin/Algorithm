#음료수 얼려먹기 (chpater5-03)

n,m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int,input()))) #공백없이 입력받기 때문에


#탐색 함수
def dfs(x,y):
    if(x<0 or x>=n or y<0 or y>=m):
        return False
    if(array[x][y]==0):
        array[x][y]=1 #방문노드
        #상하좌우 위치에 대해 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1) 
        dfs(x,y+1)
        return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count +=1

print(count)




