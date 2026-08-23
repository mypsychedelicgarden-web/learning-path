# Retry cycle for N tries.
#Выведи по строке на каждую попытку: Попытка 1 из 3...
attempts = 3
for n in range(1,attempts+1):
    print(f"Попытка {n} из {attempts}")
    