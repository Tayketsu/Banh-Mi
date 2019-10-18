from datetime import datetime, timedelta

def count_booking_streak(bookings):
    """Count the number of consecutive days that the person has entered a bookings.

    :param bookings: dictionary of booking dicts
    :return: streak (str(integer))
    """
    # Initialize streak counter
    streak = 0

    # Make sure bookings are sorted
    booking_keys = bookings.keys()
    # Sort bookings by date then reverse (we want youngest dates at the start)
    booking_keys.sort(key=lambda value: datetime.strptime(bookings[value.encode()]['date'].encode('utf-8'), "%m/%d/%Y"))
    booking_keys = booking_keys[::-1]


    # Get the current date so we can compare to the booking dates
    dtc = datetime.now()  # dtc is "Date To Check"
    delta = timedelta(days=1)

    first_booking_date = bookings[booking_keys[0]]['date']
    fwdt = datetime.strptime(first_booking_date,"%m/%d/%Y")  # fwdt = "First booking DateTime"

    # If they have worked out today, add one
    if dtc.day == fwdt.day and dtc.month == fwdt.month and dtc.year == fwdt.year:
        streak += 1
    # If they worked out yesterday, start the streak from yesterday
    if (dtc - delta).day == fwdt.day and (dtc-delta).month == fwdt.month and (dtc-delta).year == fwdt.year:
        streak += 1
        dtc = dtc-delta
    # Loop through 2nd -> last bookings
    # For each booking, add 1 if it was the next day
    pwdt = fwdt # pwdt = "Previous booking Date Time"
    for booking_key in booking_keys[1:]:
        booking = bookings[booking_key]
        booking_date = booking['date']
        wdt = datetime.strptime(booking_date,"%m/%d/%Y")  # "wdt = "booking DateTime"
        if wdt.day == pwdt.day and wdt.month == pwdt.month and wdt.year == pwdt.year:
            # They logged two bookings on the same day, don't count the streak and don't move to next day
            continue
        dtc = dtc - delta
        if dtc.day == wdt.day and dtc.month == wdt.month and dtc.year == wdt.year:
            streak += 1
        pwdt = wdt

    return str(streak)
