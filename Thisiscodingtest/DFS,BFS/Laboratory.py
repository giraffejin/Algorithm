#이것이 코딩테스트다
#Chapter12-16: DFS/BFS 기출 특정 연구소
#https://www.acmicpc.net/problem/14502

#바이러스가 확산에는 DFS를 활용하고 벽을 세우는 경우의 수는 조합 라이브러리를 활용

from itertools import combinations
import copy

n, m = map(int, input().split())
graph = [] * (n)
for i in range(n):
    graph.append(list(map(int, input().split())))

# 원본 graph를 복사해둔다(벽을 설치할때마다 그래프가 변경되기 때문에)
original = copy.deepcopy(graph)

# 벽을 세우는 함수
# 현재 빈칸인 부분을 리스트에 추가
blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
# 벽이 세워질 수 있는 모든 조합의 경우
candidates = list(combinations(blank, 3))  # 빈칸 중 3곳에 벽을 세울 수 있음


# 벽을 세우는 함수
def build_wall(candidate):
    for cx, cy in candidate:
        graph[cx][cy] = 1  # 벽을 세우기
    return graph  # 벽을 세운 그래프를 return


def dfs(x, y):  # dfs를 통해 바이러스가 퍼져나가는 것을 확인
    if (x < 0 or x >= n or y < 0 or y >= m):
        return False
    if graph[x][y] == 0:  # 이동이 가능한 곳(인접한 곳)
        graph[x][y] = 2  # 방문 처리
        # 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있음
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    return graph


# 연구소를 돌면서 dfs수행
def simulate():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:  # 바이러스가 있다면
                graph[i][j] = 0  # 이동이 가능한 곳으로
                dfs(i, j)  # dfs탐색을 통해 퍼져나가는 것 살피기
    return graph


# 안전 구역 세기
def safe(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count


# 가능한 경우의 수를 실행하며 안전 영역의 크기가 가장 클 때 찾기
result = 0
count = 0
for candidate in candidates:
    build_wall(candidate)  # 벽을 세우고
    simulate()
    result = max(result, safe(graph))
    graph = copy.deepcopy(original)  # 원래 벽 상태로 돌려놓기

print(result)

            

