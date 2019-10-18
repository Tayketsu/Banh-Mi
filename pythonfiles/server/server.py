##############################################################################
# bottle for client-server communication
import json
from bottle import run, post, request, response

# Background scheduler to run checks of recurring booking database
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

# pickle for hacking user db and booking <-> user db
import pickle

# Importing other functions that the server uses 
from control import cars_available
from api_control import create_booking_for_vehicle, create_vehicle

##############################################################################
###### Listening functions for server #######

# Listen for request for saving a recurring booking
@post('/recbook')
def recbook():
    # Get recurring booking data that was sent by the client
    booking_data = request.json
    
    # TODO: Call function to save recurring booking and return if successfull or not
    
    return json.dumps(save_recbook(booking_data))

##############################################################################
###### Recurrent server tasks scheduler #######
  
#  function that will create recurring bookings if not yet existent
def check_recurring_bookings():
    print("Checking if recurring bookings have to be updated")
    
    # Load all recurring bookings
    infile = open("recbooks",'rb')
    recbooks = pickle.load(infile)
    infile.close()
    
    #dict1={"Weekday": weekdays, "Time":date_string, "Endtime": date_stringend, "UserID": userid}
    for recbook in recbooks:
        userid = recbook["UserID"]
        # TODO: Add logic to evaluate which days in the next 30 days should have
        # a booking belonging to this recurring booking user.
        # For now we just assume that this process will yield a list of dates 
        # that we need to check
        
        # TODO: Add logic that, for all the dates at the given time, checks if 
        # any of the bookings in the database belong to the current user (using
        # the API to read bookings the given date/time-range. 
        # All dates for which no such booking exists are added to a list of bookings
        # that need to be added to the database. 
        
        # For testing purposes we assume that the two missing steps before this
        # one yield that one booking (for the day furthest from our current date)
        # is missing and has to be added
        
        missing_bookings = [["2019-10-17T19:00:00+00:00","2019-10-17T20:30:00+00:00"]]
        
        for missing_booking in missing_bookings:
            # find some available vehicle for this timeslot
            cars = cars_available(start, end)
            print(cars[0]["id"])
            add_booking(userid,missing_booking[0],missing_booking[1],cars[0]["id"])
            
    return True

# Define the background process schedule that will create recurring bookings
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_recurring_bookings, trigger="interval", seconds=10)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())



##############################################################################
###### Server functions - Reading and writing Databases #######
 # TODO: Function to remove recurring bookings if user cancels it

# Save a rec booking in its pickle file
def save_recbook(booking_data):
 
    infile = open("recbooks",'rb')
    recbooks = pickle.load(infile)
    infile.close()
    recbooks.append(booking_data) # Append new recurring booking
    outfile = open('recbooks','wb')
    pickle.dump(recbooks,outfile)
    outfile.close()
    return True

# Add a booking over the api to the ego db and to our db that matches users with bookings     

def add_booking(userid,start,end,vehicleid):
    
    # Put booking in db with API
    bookingid = create_booking_for_vehicle(vehicleid,start,end)
    if (bookingid == 0):
        return False
    
    # Put booking id in database with connection to user id
    infile = open("bookids",'rb')
    bookids = pickle.load(infile)
    infile.close()
    bookids.append({bookingid: userid})
    outfile = open('bookids','wb')
    pickle.dump(bookids,outfile)
    outfile.close()
    
    return True

##############################################################################
###### Initalize databases with fake data and start the server ####### 
    
# 1. Initalize DBs
    # Initalize the recurring bookings DB
recbooks = [] #there are no recurring bookings so far
outfile = open('recbooks','wb')
pickle.dump(recbooks,outfile)
outfile.close()

    # Initalize user-db with fake users
users = [{"userid":100, "name": "Alex",},{"userid":101, "name": "Dinh An",},
          {"userid":102, "name": "Dung",},{"userid":103, "name": "Kevin",},
          {"userid":104, "name": "Thong",}]

outfile = open('users','wb')
pickle.dump(users,outfile)
outfile.close()

    # Initialize the database that matches booking ids to the user id that owns this booking
bookids = [] #there are no bookings so far
outfile = open('bookids','wb')
pickle.dump(bookids,outfile)
outfile.close()

    # TODO: Write fake bookings
my_car = create_vehicle("DE","AC-1230","e.Go","blub300","blub300")
add_booking(100,"2019-10-17T19:00:00","2019-10-17T20:30:00",my_car)

    
    
# 2. Run server
run(host='localhost', port=8080, debug=True)







# =============================================================================
# ##EXAMPLE: How to define post and call functions with recieved data
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# 
# @post('/process')
# def my_process():
#   #req_obj = json.loads(request.body.read())
#   x = request.json.get('name')
#   # do something with req_obj
#   # ...
#   print(x)
#   return json.dumps(thisdict)
# =============================================================================