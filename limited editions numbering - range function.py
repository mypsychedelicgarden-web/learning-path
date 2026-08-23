#лимитированный тираж нужно пронумеровать — 1/25, 2/25, … Задача «повторить действие N раз со счётчиком» — базовая рабочая рутина.
#Выведи ярлык на каждый экземпляр тиража: Self-Reflection 1/5 … Self-Reflection 5/5
title    = "Self-Reflection"
editions = 5
for n in range(1,editions+1):
    print(f"{title} {n}/{editions}")
    