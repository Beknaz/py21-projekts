from .models import *
from .serializers import *
import decimal
from decimal import Decimal
body_types = ["sedan", "universal", "kupe", "hetchbeck", "miniwen", "vnedorojnik", "pikap"]
def create():
    marka = input("Укажите марку: ")
    model = input("Укажите модель: ")
    yers = int(input("Укажите год: "))
    valume = round(float((input("Укажите объём двигателя: "))), 1)
    color = input("Укажите цвет: ")
    print("Выберите тип кузова: ")
    for type in body_types:
        print(f"* {type}")
    body_t = input("==================================\nВыберите тип кузова: ")
    if body_t in body_types:
        kuzov = body_t
    else:
        raise Exception("Такого типа не существует")
    probeg = int(input("Укажите пробег: "))
    price = round(float((input("Укажите цену: "))), 2)
    Car(marka, model, yers, valume, color, kuzov, probeg, price)
    return "Машина успешно добавлена"

def listing():
    serializer = CarSerializer()
    cars = serializer.serialize_queryset()
    return cars

def retrieve(p_id):
    car = obj_404(Car, "id", int(p_id))
    serializer = CarSerializer()
    return serializer.serialize_obj(car)


def update(p_id):
    car = obj_404(Car, "id", int(p_id))
    field = input("Что вы хотите изменить?: ")
    if field in dir(car):
        print(f"старое значение: {getattr(car, field)}")
        value = input(f"{field} = ")
        setattr(car, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return retrieve(p_id)


def delete(p_id):
    car = obj_404(Car, "id", int(p_id))
    Car.objects.remove(car)
    return "Продукт успешно удален"

def comment():
    print("Выберите продукт:")
    for p in Car.objects:
        print(p.marka, p.model)
    model = input("===============\nукажите модель: ")
    car = obj_404(Car, "model", model)
    body = input("Введите коммент: ")
    Comment(car, body)
    return 'Комментарий успешно добавлен'
