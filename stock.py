#Дано 3 списка, Напиши цикл for с zip(), который для каждой работы посчитает, сколько экземпляров осталось в наличии (edition - sold), и выведет красивый текст.
artworks = ["Self-Reflection", "Panspermia", "Dewdrop Mirror"]
editions = [25, 10, 15]
sold = [18, 10, 4]
for artwork_name, edition, sold_amount in zip(artworks,editions,sold):
        print(f"I have in stock {edition-sold_amount} prints of {artwork_name}.")
        