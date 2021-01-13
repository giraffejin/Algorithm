#도시 분할 계획 (chapter10-03)

import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m = map(int,input().split())

#부모 테이블 초기화
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

#간선 관련 정보 받기
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

#비용이 낮은 순서로 정렬
edges.sort()
result = 0
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

#간선들에 대해서 최소 비용을 구성할 수 있는 최소 신장 트리 찾기
for edge in edges:
    cost,a,b = edge
    if(find_parent(parent,a)!=find_parent(parent,b)):
        union_parent(parent,a,b)
        result +=cost
        last = cost #최소 비용부터 처리되기 때문에 가장 크기가 큰 비용의 값으로 갱신됨

#최소한의 비용으로 2개의 신장 트리로 분할하기 위해 최소 신장 트리를 구성한 후 간선 중에서 가장 비용이 큰 간선을 제거
print(result-last)