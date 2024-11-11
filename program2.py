def decode_message( s: str, p: str) -> bool:

# write your code here
    msg_len, pat_len = len(s), len(pattern)
    dp_table = [[False] * (pat_len + 1) for _ in range(msg_len + 1)]
    
    dp_table[0][0] = True
    
    for col in range(1, pat_len + 1):
        if pattern[col - 1] == '*':
            dp_table[0][col] = dp_table[0][col - 1]
    
    for row in range(1, msg_len + 1):
        for col in range(1, pat_len + 1):
            if pattern[col - 1] == '*':
                dp_table[row][col] = dp_table[row][col - 1] or dp_table[row - 1][col]
            elif pattern[col - 1] == '?':
                dp_table[row][col] = dp_table[row - 1][col - 1]
            else:
                dp_table[row][col] = dp_table[row - 1][col - 1] and s[row - 1] == pattern[col - 1]
    
    return dp_table[msg_len][pat_len]
