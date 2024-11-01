# Фокеева Инна, 23-я когорта — Финальный проект. Инженер по тестированию расширенный


headers = {
    "Content-Type": "application/json"
}

# Создание заказа
order_body = {
    "firstName": "Инна",
    "lastName": "Фокеева",
    "address": "Москва, ул Ленина, 5",
    "metroStation": 5,
    "phone": "+7 927 456 35 35",
    "rentTime": 2,
    "deliveryDate": "2024-10-31",
    "comment": "Все получится!",
    "color": [
        "BLACK"
    ]
}

# Получение заказа по треку
t_number = {
    "track": 123456
}