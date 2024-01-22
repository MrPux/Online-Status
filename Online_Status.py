#   Write a function named 'online_count' that takes one parameter. 
#   The parameter is a dictionary that maps from strings of names to the string "online" or "offline".

#   Function should return the number of people who are online

def online_count(statuses):
    count =  [statuses[i] for i in statuses].count("online") 
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }     
print(online_count(statuses)) #It prints 2