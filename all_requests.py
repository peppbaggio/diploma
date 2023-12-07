import configuration
import data
import requests

def order_create():
    return requests.post(configuration.SERVER_URL + configuration.ORDER_CREATE_URL, json=data.ORDER_BODY)

def get_track_from_order():
     track = order_create().json()
     return str(track['track'])

def get_info_from_track():
    params_request = {'t': get_track_from_order()}
    return requests.get(configuration.SERVER_URL + configuration.GET_ORDER_INFO_URL, params=params_request)
