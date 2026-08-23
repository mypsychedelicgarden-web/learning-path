#клиент кладёт в корзину несколько работ — нужно посчитать итог. Это самый частый паттерн в реальном коде: пробежать список и что-то накопить.
order = [600.60, 450.00, 720.50]
total = sum(order)
Amount = len(order)
print(f"{Amount} artworks for {total:.2f} Euro")
#another way
t=0
for item_price in order:
    t=t+item_price
print(f"{Amount} artworks for {t:.2f} Euro")
