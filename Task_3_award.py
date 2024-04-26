swim_time = int (input ("Enter swimming time: "))
cycle_time = int (input ("Enter cycling time: "))
run_time = int (input ("Enter running time: "))
total_time = swim_time + cycle_time + run_time

print ("The total time is " + str(total_time) + " minutes")

if total_time <= 100:
    print ("Provincial colours")
elif total_time <=105:
    print ("Provincial half colours")
elif total_time <=110:
    print ("Provincial scroll")
else:
    print ("No award")
