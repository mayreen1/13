# 13
Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:

1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.

2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:

Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
От 18 до 25 лет — 990 руб.
От 25 лет — полная стоимость 1390 руб.
3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.

Решение:

number_of_tickets = int(input("Укажите количество билетов: "))
ages = []
for i in range(0, number_of_tickets):
    age = int(input("Укажите возраст посетителя: "))
    ages.append(age)

    def prise(age):
            if age < 18:
                return 0
            elif 18 <= age < 25:
                return 990
            else:
                return 1390

    total_price = sum(map(prise, ages))

discount = int(total_price * 0.9)
if number_of_tickets > 3:
    print("Стоимость всех билетов со скидкой: ", discount, "руб.")
else:
    print("Стоимость всех билетов: ", total_price, "руб.")