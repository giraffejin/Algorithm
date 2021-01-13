#팀 결성 (chapter10-02)

n,m = map(int,input().split())

parent =[0]*(n+1)

#parent값 초기화
for i in range(n):
    parent[i] = i

#루트 노드 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#합집합 구성하기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#m개의 연산을 입력 받아 처리
for i in range(m):
    op,a,b = map(int,input().split())
    if(op==0):
        union_parent(parent,a,b)
    elif(op==1):
        ra = find_parent(parent,a)
        rb = find_parent(parent,b)
        if(ra==rb):
            print('YES')
        else:
            print('NO')
