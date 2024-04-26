str_manip = input ("Please enter a sentence:\n")
length = len(str_manip)
print ("Length of string is", length)
last_letter = (str_manip[length-1:])
new_text = ""
for x1 in str_manip:
    y1 = x1
    if x1 == last_letter:
        y1 = "@"
    new_text = new_text + y1
print (new_text)

end_reversed = ""
for x2 in range(3):
    end_reversed = end_reversed + str_manip[length-1-x2:length-x2]
print (end_reversed)

new_word = str_manip[:3] + str_manip[length-2:]
print (new_word)

        
