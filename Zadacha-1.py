price = 0
tickets = int(input('Введите количество билетов: '))
for i in range(tickets):
    i += 1
    age_ticket = int(input(f'Введите Ваш возраст, для расчета стоимости билета {i}: '))
    if age_ticket < 18:
            print('Поздравляем! Ваш билет бесплатный!)')
    elif 18 <= age_ticket < 25:
            price += 990
            print('Стоимость билета - 990 руб.')
    else:
            price += 1390
            print('Стоимость билета - 1390 руб.')

if tickets > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате - {price} руб. (Вы зарегистрировали больше 3-х человек, Ваша скидка составила 10%)')
else:
    print(f'Сумма к оплате - {price} руб.')
