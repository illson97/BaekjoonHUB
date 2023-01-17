N, M = map(int, input().split())
    
if (max(N, M) - min(N, M)) > 0:
    print(max(N, M) - min(N, M))
        
if (max(N, M) - min(N, M)) < 0:
    print(-(max(N, M) - min(N, M)))