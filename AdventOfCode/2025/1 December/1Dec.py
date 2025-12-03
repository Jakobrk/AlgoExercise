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

        #print(line)
        
        
        # Process the line (e.g., print or update counter)
        
        l_or_r = line[0]
        number = int(line[1:])
        
        #print(l_or_r)
        #print(number)

        if l_or_r == "R":
            dial = dial + number
            while dial >= 100:
                dial = dial - 100
        else:
            dial = dial - number
            while dial < 0:
                dial = dial + 100

        #print(dial)

        if dial == 0:
            counter = counter + 1

print("counter: ", counter)

