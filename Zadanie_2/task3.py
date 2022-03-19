
month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

sez = ["Winter", "Spring", "Summer", "Fall"]

mes = int(input("Введите месяц: "))
if mes == 1 or mes == 2 or mes == 12:
    print(sez[0])
elif mes == 3 or mes == 4 or mes == 5:
    print(sez[1])
elif mes == 6 or mes == 7 or mes == 8:
    print(sez[2])
elif mes == 9 or mes == 10 or mes == 11:
    print(sez[3])
else:
    print("Нет такого месяца")

print(month[mes])



#year_seas = {
    #"Winter": ['December', 'January', 'February'],
    #"Spring": ['March', 'April', "May"],
    #"Summer": ['June', 'July', 'August'],
    #"Fall": ['September', 'October', 'November']
#}

#"January": 1,
    #"February": 2,
    #"March": 3,
    #"April": 4,
    #"May": 5,
    #"June": 6,
    #"July": 7,
    #"August": 8,
    #"September": 9,
    #"October": 10,
    #"November": 11,
    #"December": 12,