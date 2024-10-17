
def isPalindrome(str):
    
    n = len(str)
    
    lo, hi = 0, n-1
    
    while lo < hi:
        
        if not str[lo].isalnum():
            lo += 1
            continue
        elif not str[hi].isalnum():
            hi -= 1
            continue
        elif str[lo].lower() == str[hi].lower():
            lo, hi = lo+1, hi-1
        else:
            return -1
    return True





str = "A man, a plan, a canal: Panama"
result = isPalindrome(str)

if result == True:
    print("Valid")
else:
    print("Invalid")

