def max_gift_voucher(N, K, G, P):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if P[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - P[i - 1]] + G[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][K]




if __name__ == "__main__":
    
    N, K = map(int, input().split())
    G = list(map(int, input().split()))
    P = list(map(int, input().split()))

    result = max_gift_voucher(N, K, G, P)
    print(result)