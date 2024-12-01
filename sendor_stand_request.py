# Ташкинова Яна, 23-я когорта — Дипломный проект

import configuration
import requests
import data

# Автотест

def test_order_creation_and_retrieval():
    response = create_order_request(data.order_body)
    track_number = response.json()["track"]
    # Далее вывод данных "Заказ создан. Номер трека:", track_number
   
 # Получение данных заказа по треку
    order_response = get_order_request(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    # Далее вывод данных Данные заказа, order_data

# Создание заказа

def create_order_request(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)
    
# Получение заказа по номеру трекера
def get_order_request(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response
