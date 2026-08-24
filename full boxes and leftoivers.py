#товар едет коробками фиксированного размера, нужно понять число полных коробок и остаток.
#Для каждого товара выведи: открытки: 10 полных коробок, остаток 10
products   = ["открытки", "постеры", "мини-принты"]
quantities = [25, 12, 205]
per_box    = 12
for product,quantity in zip(products,quantities):
    boxes = quantity//per_box
    leftovers = quantity%per_box
    if boxes == 1 and leftovers == 1:
        print(f"{product}: {boxes} full box, left {leftovers} piece")
    elif boxes == 1 and leftovers != 1:
        print(f"{product}: {boxes} full box, left {leftovers} pieces")
    elif boxes != 1 and leftovers == 1:
            print(f"{product}: {boxes} full boxes, left {leftovers} piece")    
    else:
        print(f"{product}: {boxes} full boxes, left {leftovers} pieces")
    



    