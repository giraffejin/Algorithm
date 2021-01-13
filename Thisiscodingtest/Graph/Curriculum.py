#커리큘럼 (chapter10-04)

from collections import deque

n = int(input())
indegree = [0]*(n+1)
#간선 정보를 담기 위한 연결 리스트 초기화
graph =[[] for i in range(n+1)]

#강의 시간을 담을 리스트와 결과 리스트
cost =[0]*(n+1)
result = [0]*(n+1)

#그래프 정보 입력 받기
for i in range(1,n+1):
    a = list(map(int, input().rstrip('-1').split())) #-1을 제외한 나머지 입력
    cost[i] = a[0]
    if len(a)>=2:
        for j in range(1,len(a)):
            graph[a[j]].append(i) #a[j]에서 i로 이동 가능
            indegree[i]+=1 #i기준 진입차수 증가

#위상 정렬 함수
def topology_sort():
    q = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
            result[i] = cost[i] #초기에 진입차수가 0인 노드


    while q:
        now = q.popleft()
        #해당 노드와 인접한 노드간의 간선을 제거
        for i in graph[now]:
            indegree[i]-=1
            result[i] = max(result[i], result[now] + cost[i])
            
            if indegree[i]==0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()