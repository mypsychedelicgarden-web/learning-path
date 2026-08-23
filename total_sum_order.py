#клиент кладёт в корзину несколько работ — нужно посчитать итог. Это самый частый паттерн в реальном коде: пробежать список и что-то накопить.
order = [600.60, 450.00, 720.50]
total = sum(order)
print(f"Summ {total:.2f}")
#another way
t=0
for item_price in order:
    t=t+item_price
print(f"Total order {t:.2f}")
