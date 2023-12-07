#Анна Сидякина, 11-я когорта — Дипломный проект. Инженер по тестировнию плюс

import all_requests
import pytest

def test_get_info_from_track():
    #Arrange

    #Act
    get_order_info = all_requests.get_info_from_track()

    #Assert
    assert get_order_info.status_code == 200, f"Expected 200, but actual status code is {get_order_info.status_code}"

