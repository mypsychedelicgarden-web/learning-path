# print("Hej! Hello from My Psychedelic Garden!")
print("Hej! Hello from My Psychedelic Garden!")
artwork_title = "Self-Reflection"
artwork_edition_number = 25
artwork_price = 600.60
print(artwork_title, "edition", artwork_edition_number, "price", artwork_price)
print(f"Fine art print by Inna Etuvgi '{artwork_title}' is printed in edition of {artwork_edition_number} and is priced at {artwork_price:.2f} EUR.")
#вводим операции с переменными - и выводим, например предложение цены со скидкой 10% на печать
print(f"the artwork price with 10% discount is {artwork_price * 0.9:.2f} EUR.")
collections = ["ALIEN", "InnerSpace", "Wonderland"]
works = [12, 8, 15]
editions = 25
for title, count in zip(collections, works):
print(f"Collection {title} contains {count*editions} prints")
