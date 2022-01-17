age = int(input()) 
height = float(input()) 
weight = float(input()) 

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")

else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)
        
    if age < 45:
        if bmi < 18.5:
            description = "недостаточной массой тела."
        elif 18.5 <= bmi <= 24.99:
            description = "нормальной массой телa."
        elif 25 <= bmi <= 29.99:
            description = "избыточной массой тела."
        else:
                if bmi >= 30:
                    description = "ожирением."
        
    else:
        if age >= 45: 
            if bmi < 22:
                description = "недостаточной массой тела."
            elif 22 <= bmi <= 26.99:
                description = "нормальной массой телa."
            elif 27 <= bmi <= 31.99:
                description = "избыточной массой тела."
            else:
                if bmi >= 32:
                    description = "ожирением."

print("bmi=", bmi, "Вы относитесь к группе людей с", description)