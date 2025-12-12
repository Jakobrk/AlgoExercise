test_cases = int(input())

for _ in range(test_cases):
    s = input().strip()
    n = len(s)
    
    # Check for om der findes uendelig-svømmetid
    infinite = False
    
    for i in range(n):
        if s[i] == '*':
            # * ved siden af *
            if i > 0 and s[i-1] == '*':
                infinite = True
                break
            if i < n-1 and s[i+1] == '*':
                infinite = True
                break
            # >*,  strømmen leder til en stjerne vi kan svømme tilbage fra
            if i > 0 and s[i-1] == '>':
                infinite = True
                break
            # *< modsat ovenfor
            if i < n-1 and s[i+1] == '<':
                infinite = True
                break
        
        # ><, vi can bounce uendeligt
        if s[i] == '>' and i < n-1 and s[i+1] == '<':
            infinite = True
            break
        
        # ><, fra den anden side  
        if s[i] == '<' and i > 0 and s[i-1] == '>':
            infinite = True
            break
    
    if infinite:
        print(-1)
        continue
    
    # Find længste sequence en vej
    # Stjener kan være wildcards
    max_length = 0
    
    # Find længste mod right 
    i = 0
    while i < n:
        if s[i] in '>*':
            count = 0
            # Tæl så længe vi ser > eller *
            while i < n and s[i] in '>*':
                count += 1
                i += 1
            # Kun tæl sekvensen hvis den indeholder mindst én >
            if '>' in s[i-count:i]:
                max_length = max(max_length, count)
        else:
            i += 1
    
    # Find længste mod venstre 
    i = 0
    while i < n:
        if s[i] in '<*':
            count = 0
            # Tæl så længe vi ser < eller *
            while i < n and s[i] in '<*':
                count += 1
                i += 1
            # Kun tæl sekvensen hvis den indeholder mindst én <
            if '<' in s[i-count:i]:
                max_length = max(max_length, count)
        else:
            i += 1
    
    # Edge case: string er kun én stjerne
    if n == 1 and s[0] == '*':
        max_length = 1
    
    print(max_length)





"""
test input:
4
*****
<<<>
>*<
*

output:
-1
3
-1
1


"""











