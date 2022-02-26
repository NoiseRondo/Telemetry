
import datetime

time = int(input('Введите время в секундах: '))
secs = 0
mins = 0
hours = 0

while time > 0:
    secs += 1
    if secs > 59:
        mins += 1
        secs = 0
    if mins > 59:
        hours += 1
        mins = 0
    time -= 1
print(hours, mins, secs)

answer = datetime.datetime(1, 1, 1, hour=hours, minute=mins, second=secs)
print("Время в чч:мм:сс", answer.strftime("%X"))

# minutes = math.floor(time/60)
#print('минут', minutes)
#hours = math.floor(time/3600)
#print('часов', hours)



