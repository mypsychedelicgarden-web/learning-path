#У тебя есть 27 готовых арт-принтов. Каждая защитная коробка вмещает ровно 5 принтов
#Сколько полных коробок получится сформировать?
#Сколько принтов останется без коробки и потребуют отдельной упаковки?
total_prints = 27
box_capacity = 5
full_boxes = total_prints // box_capacity
remaining_prints = total_prints % box_capacity
print(f"Number of full boxes: {full_boxes}")
print(f"Remaining prints: {remaining_prints}")
