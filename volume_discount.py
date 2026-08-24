#Скидка по объёму заказа
#10 шт и больше → скидка 20%
#от 5 до 9 → скидка 10%
#меньше 5 → без скидки
#Посчитай и выведи итоговую цену за штуку с учётом скидки (с :.2f).
quantity = 3
price = 100
if quantity >= 10:
    print(f"You order {quantity} pieces, your price with the discount is {price*0.8:.2f}")
elif quantity >= 5:
    print(f"You order {quantity} pieces, your price with the discount is {price*0.9:.2f}")
else:
     print(f"You order {quantity} pieces, your price with the discount is {price:.2f}")
     