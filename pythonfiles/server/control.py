import api_control as api
import datetime
import dateutil.parser


def date1_greater(timeA, timeB):
    #returns True if first date is at a later time
    #2019-10-17T17:30:00
    date1 = dateutil.parser.parse(timeA)
    date2 = dateutil.parser.parse(timeB)

    return (date1 > date2)

def booking_overlap(start1, end1, start2, end2):
    #2019-10-17T17:30:00
    #(StartA <= EndB) and (EndA >= StartB)
    return (date1_greater(end2, start1) and date1_greater(end1, start2))

def cars_available(start, end):
    """
    Checks which cars are available in a time intervall

    ...

    Attributes
    ----------
    start : str
        start date in iso format 
        # example : 2019-10-17T17:30:00
    end : str
        the name of the animal
        # example : 2019-10-17T17:30:00

    Returns
    -------
    list
        avaliable list of cars with id and license plate
    """

    vehicles = api.all_vehicles()
    for car in list(vehicles):
        for books in list(api.all_bookings_of_vehicle(car['id'])):
            if (False == booking_overlap(start, end, books['from'], books['until'])):
                vehicles.remove(car)
                break
    
    return vehicles

def book_vehicle(vehicle_id, start, end):
    """
    Books car for time interval

    ...

    Attributes
    ----------
    id : str
        id of vehicle
    
    start : str
        start date in iso format 
        # example : 2019-10-17T17:30:00

    end : str
        the name of the animal
        # example : 2019-10-17T17:30:00

    Returns
    -------
    boolean
        if booking could be made
    """
    return api.create_booking_for_vehicle(vehicle_id, start, end)

