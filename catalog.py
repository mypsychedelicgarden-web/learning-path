# Есть Три параллельных списка. 
#По каждой работе выведи строку: название, цена с НДС (2 знака), размер тиража. Например: Self-Reflection — 750.00 EUR (с НДС) — тираж 25
titles   = ["Self-Reflection", "Dream Big", "ALIEN"]
prices   = [600.00, 450.00, 720.00]
editions = [25, 10, 30]
vat      = 0.25
for title, price, edition in zip(titles,prices,editions):
    print(f"{title} - {price*(1+vat):.2f} EUR (с НДС) — тираж {edition}")
    