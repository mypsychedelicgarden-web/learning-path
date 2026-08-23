#Посчитай цену после скидки, потом добавь НДС, и выведи одной строкой весь путь: Цена: 600.00 EUR → со скидкой 10%: 540.00 EUR → с НДС 25%: 675.00 EUR
price    = 600.00
discount = 0.10   # 10%
vat      = 0.25   # moms 25%
dis_price = price*(1-discount)
price_vat = dis_price*(1+vat)
print(f"Цена: {price:.2f} EUR → co скидкой 10%: {dis_price:.2f} EUR → с НДС 25%: {price_vat} EUR")
