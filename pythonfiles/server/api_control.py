import json
import requests

urlbase =  "https://ego-vehicle-api.azurewebsites.net"

##urlbase = 'http ://localhost'
##key = 'ego'
key ='8996cc48-dba5-48fe-9546-0ac3146f385f'



def all_vehicles():
    resp = requests.get(urlbase + '/api/v2/vehicles', headers={'X-Api-Key': key})
    dat = resp.json()['data']
    return dat

def create_vehicle(country, licenceplate, manufacturer, model, name):
    data = {"country": country, "licensePlate": licenceplate, "manufacturer": manufacturer, "model": model, "name": name}

    resp = requests.post(url = (urlbase + '/api/v2/vehicles'), json = data, headers={'X-Api-Key': key})
    
    if(resp.json()['success']):
        return resp.json()['data']['id']
    return False

def create_booking_for_vehicle(vehicle_id, start, end):
    data = {
        "from" : start, "until" : end
        }    
    
    resp = requests.post(url = (urlbase + '/api/v2/vehicles/' + vehicle_id +'/bookings' ), json = data, headers={'X-Api-Key': key})

    if( resp.json()['success']):
        return resp.json()['data'][0]['id']
    return False


def all_bookings_of_vehicle(vehicle_id):
    resp = requests.get(urlbase + '/api/v2/vehicles/' + vehicle_id +'/bookings', headers={'X-Api-Key': key})
    dat = resp.json()['data']
    return dat


def start_booking(booking_id):
    resp = requests.post(url = (urlbase + '/api/v2/bookings/' + booking_id +'/start' ), headers={'X-Api-Key': key})
    succ = resp.json()['success']
    return succ
    

def finish_booking(booking_id):
    resp = requests.post(url = (urlbase + '/api/v2/bookings/' + booking_id +'/finish' ), headers={'X-Api-Key': key})
    succ = resp.json()['success']
    return succ


def cancel_booking(booking_id):
    resp = requests.post(url = (urlbase + '/api/v2/bookings/' + booking_id +'/cancel' ), headers={'X-Api-Key': key})
    succ = resp.json()['success']
    return succ
#%%

def sequential_booking():
    return 0

