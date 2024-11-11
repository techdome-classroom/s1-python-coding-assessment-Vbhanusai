def decode_message( s: str, p: str) -> bool:

# write your code here
    msg_len, pat_len = len(s), len(p)
    dp = [[False] * (pat_len + 1) for _ in range(msg_len + 1)]
    
    dp[0][0] = True
    
    for col in range(1, pat_len + 1):
        if p[col - 1] == '*':
            dp[0][col] = dp[0][col - 1]
    
    for row in range(1, msg_len + 1):
        for col in range(1, pat_len + 1):
            if p[col - 1] == '*':
                dp[row][col] = dp[row][col - 1] or dp[row - 1][col]
            elif p[col - 1] == '?':
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = dp[row - 1][col - 1] and s[row - 1] == p[col - 1]
    
    return dp[msg_len][pat_len]
