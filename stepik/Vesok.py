x = int(input("Введите дату "))
if x <= 0:
    print("Введены неорректные данные")
elif x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    description = "данный год является високосным"  
else:
    description = "данный год является не високосным"
print(x, ";", description)