N = int(input())
M = int(input())
graph = [[]*N for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
cnt = 0
visit = [0] * (N+1)

def dfs(start) : 
    global cnt
    visit[start] = 1
    for i in graph[start] :
        if visit[i] == 0:
            dfs(i)
            cnt += 1
            
dfs(1)
print(cnt)