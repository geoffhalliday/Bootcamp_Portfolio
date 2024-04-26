cafe = ["tea","coffee","cake","sandwiches"]
stock = {
    "tea": 50,
    "coffee": 60,
    "cake": 20,
    "sandwiches" : 40
    }
price = {
    "tea": 1.5,
    "coffee": 1.6,
    "cake": 2.5,
    "sandwiches": 2
    }
item_value = 0
for x in cafe:
    item_value += (stock[x] * price[x])

print ("The total value of stock is £{}.".format("%.2f" % item_value))

        
    

    
        
    
    
