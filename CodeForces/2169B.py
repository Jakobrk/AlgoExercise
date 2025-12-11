#https://codeforces.com/problemset/problem/2169/B?fbclid=IwZXh0bgNhZW0CMTAAYnJpZBEwOTRRYmd3NXhTa2FHRTQwcXNydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR4pVG6EAzFJa0__xm1-fUi94Fyneam-LDXEZR-RqfymtcGzHYXm25MH1LtCJQ_aem_8bnXlZLNqPNpSX-2FWVx4A



test_cases = int(input())


for ppp in range(test_cases):

    river = list(input())
    n = len(river)
    
    river = ["L"] + river + ["R"]

    print(river)
    #print(n)

    max_strokes = 0

    for start_pos in range(n+2):
        if river[start_pos] == "L" or river[start_pos] == "R":
            continue
        
        #altid uendeligt
        if river[start_pos] == "*":
            if river[start_pos-1] == ">" or river[start_pos+1] == "<" or river[start_pos-1] == "*" or river[start_pos+1] == "*":
                max_strokes = -1
                break

        #string er 1 lang
        if river[start_pos-1] == "L" and river[start_pos+1] == "R":
            max_strokes == 1
            break

        
    










    print(max_strokes)





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











