counter = 0
dial = 50

#testlines = 11

#Open and iterate through each line
with open('./input.txt') as f:
    for line in f:
        line = line.strip()  # Remove whitespace/newlines

        #testlines = testlines - 1
        #if testlines == 0:
        #   break
        
        
        l_or_r = line[0]            #R or L
        number = int(line[1:])      #Rest of the input (number)
        
        #print(l_or_r)
        #print(number)

        if l_or_r == "R":
            print("R")
            
        else:
            print("L")

        

print("counter: ", counter)

