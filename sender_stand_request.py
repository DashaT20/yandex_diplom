import configuration
import requests
import data

def post_new_order(): # запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставялем полный url
                         json=data.order_body)  # а здесь тело


def get_orders_track(track): # запрос на получение заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + str(track))


