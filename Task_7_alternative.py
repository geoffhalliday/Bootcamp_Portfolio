sample = "This is the text which WILL be manipulated"

capital = True
new_text_1 = ""

for x in sample:
    if capital == True:
        char = x.upper()
        capital = False
    else:
        char = x.lower()
        capital = True
    new_text_1 += char
print (new_text_1)

text_list = sample.split()
capital = True

for x in range(len(text_list)):
    if capital == True:
        text_list[x] = text_list[x].lower()
        capital = False
    else:
        text_list[x] = text_list[x].upper()
        capital = True
new_text_2 = " ".join(text_list)
print (new_text_2)

        
    

    
        
    
    
