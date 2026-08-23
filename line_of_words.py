#Собери из списка одну строку через запятую.
names = ["Anna", "Bo", "Chen"]
line=""
comma=","
for name in names:
    line=line+name+comma
print(line)
