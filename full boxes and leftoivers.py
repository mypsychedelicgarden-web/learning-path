#товар едет коробками фиксированного размера, нужно понять число полных коробок и остаток.
#Для каждого товара выведи: открытки: 10 полных коробок, остаток 10
products   = ["открытки", "постеры", "мини-принты"]
quantities = [130, 47, 205]
per_box    = 12
for product,quantity in zip(products,quantities):
    print(f"{product}: {quantity//per_box} full boxes, left {quantity%per_box} pieces")
    