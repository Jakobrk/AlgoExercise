#Problem at: https://codeforces.com/problemset/problem/404/A


n = int(input())                                #dimensionerne af NxN matrix

rows = [input().strip() for _ in range(n)]      #['xooox', 'oxoxo', 'soxoo', 'oxoxo', 'xooox']

matrix = [list(row[:n]) for row in rows]        #[['x', 'o', 'o', 'o', 'x'], ['o', 'x', 'o', 'x', 'o'], ['s', 'o', 'x', 'o', 'o'], ['o', 'x', 'o', 'x', 'o'], ['x', 'o', 'o', 'o', 'x']]

if matrix[0][0] == matrix[0][1]:
    print("NO")  #de to første bokstaver er ens
    exit()

x_letter = matrix[0][0]
other_letter = matrix[0][1]


for i in range(n):
    if i == 0:
        if matrix[i][i] == matrix[i][-1] and matrix[i][i] == x_letter:  #når i = 0 har vi også -0
          for j in range(n):           #fra start til i
            if j == i  or  j == n-(i+1):
                continue

            if matrix[i][j] != other_letter:
                print("NO")
                #print("otherletter on", i, j)
                #print("fejl i andrebokstaver i række: ", i, "bokstav nummer: ", j, ",bokstaverne: ", matrix[i][j], " og ", other_letter)
                exit()
            else:
                continue
        else:
            print("NO")
            #print("test af 1, og sidste i første omgang")
            exit()
          
    if matrix[i][i] == matrix[i][-(i+1)] and matrix[i][i] == x_letter: #check at x-bokstavet er det samme
        #print("i og -i stemmer i række: ", i)

        for j in range(n):           #fra start til i
            if j == i  or  j == n-(i+1):
                continue

            if matrix[i][j] != other_letter:
                print("NO")
                #print("otherletter on", i, j)
                #print("fejl i andrebokstaver i række: ", i, "bokstav nummer: ", j, ",bokstaverne: ", matrix[i][j], " og ", other_letter)
                exit()
            else:
                continue
    else:           #første og sidste x-bokstav er ikke ens, eller det matcher ikke x-letter.
        print("NO") 
        #print(matrix[i][i], matrix[i][-i])
        exit()

print("YES")




"""
5
abcda
bacad
bcade
eaeae
afffa


"""

