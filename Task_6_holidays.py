# It seemed more efficient to create functions without the use of parameters
# which is what I have done with hotel_cost and holiday_cost.
# However, I have shown the use of a parameter for car_rental just to show the
# alternative method (which might have been the expectation).
# For plane_cost I chose to use a parameter as it looked neater.

# This function calculates hotel cost based on number of nights stayed:
def hotel_cost ():
    return num_nights * 50 # £50 per night holiday cost

# This function calculates plane cost based on city destination
def plane_cost (x):
    if x == "Madrid":
        return 500
    elif x == "Paris":
        return 400
    elif x == "New York":
        return 1500

# This function calculates car rental cost based on number of rental days
def car_rental (x):
    return x * 20 # £20 per day car rental cost

# This function calculates total holiday cost (hotel_cost + plane_cost + car_rental)
def holiday_cost (): # no parameters used 
    return hotel_cost() + plane_cost(city_flight) + car_rental(rental_days)

# User inputs number to select destination city
# The 'choice' variable is not necessary - 'city_flight' could be used at the input stage
# But that would mean either city_flight would store a number, which would make it harder to understand the plane_cost function, 
# or the input would be less user friendly (full place name needed instead of just a number)
print ("Choose you city to fly to")
print ("1 - Madrid")
print ("2 - Paris")
print ("3 - New York")
city_flight = ""
while True:
    choice = input ("Enter number to choose: ")
    if choice == "1":
        city_flight = "Madrid"
    elif choice == "2":
        city_flight = "Paris"
    elif choice == "3":
        city_flight = "New York"
    else:
        print ("Invalid choice - select again")
    if city_flight != "":
        break

# User inputs number of nights of stay, ad number of car rental days
num_nights = int (input ("Enter the number of nights for your hotel stay: "))
rental_days = int (input ("Enter the number of days car hire: "))

# Cost are calculated by calling on relevant funcitons
hotel = hotel_cost () # calling function to calculate hotel cost
plane = plane_cost (city_flight) # calling function to calculate plane cost
car = car_rental (rental_days) # calling function to calculate car rental cost
total_cost = holiday_cost () # calling function to calculate total cost of holiday

# Displays total cost of holiday, and a breakdown of the costs
print ()
print (f"The total cost of your holiday in {city_flight} is £{str(total_cost)}.")
print ("The breakdown of the cost of your holiday is as follows:")
print (f"The cost of your flight to {city_flight} is £{str(plane)}.")
print (f"The cost of {str(num_nights)} nights in a hotel is £{str(hotel)}.")
print (f"The cost of {str(rental_days)} days car hire is £{str(car)}.")


    
