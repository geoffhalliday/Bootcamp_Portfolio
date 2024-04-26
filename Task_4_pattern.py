pattern = ""

for x in range (9):
    if x < 5:
        pattern += "*"
        print (pattern)
    else:
        print (pattern[x-4:])
    
