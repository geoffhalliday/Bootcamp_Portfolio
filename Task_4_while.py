total = 0
count = 0

while True:
    num = input ("Enter a number: ")
    if num == "-1":
        break
    total += float(num)
    count += 1

average = (total/count)
print (f"The average is {average}")

