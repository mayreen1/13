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
