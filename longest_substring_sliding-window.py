def longestSubstring(str):
    
    l = 0
    longest = 0
    sett = set()
    n = len(str)
    
    for r in range(n):
        
        while str[r] in sett:
            sett.remove(str[l])
            l += 1
        
        window_length = (r - l) + 1
        longest = max(longest, window_length)
        sett.add(str[r])
    
    return longest


str = "bbbbbbb"
result = longestSubstring(str)
print(result)

# Time: O(n)
# Space : O(n)