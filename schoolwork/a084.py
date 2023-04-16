def ca(n):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1] = [1, 1, 1]  
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][1] + dp[i-1][2]
        if i >= 3:
            dp[i][1] = dp[i-2][0] + dp[i-2][2]
            dp[i][2] = dp[i-2][0] + dp[i-2][1]
    return sum(dp[n])

try:
    while(1):
        print(ca(int(input())))
except EOFError as e:
   print(end="")

