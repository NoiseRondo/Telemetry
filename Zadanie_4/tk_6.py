
predm = {"Информатика": 170, "Физика": 40, "Физкультура": 30}

try:
    with open('slov.txt', 'r') as file:
        for line in file.readlines():
            data = line.replace('(', ' ').split()

            predm[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
except IOError as e:
    print(e)
except ValueError:
    print("")

print(predm)
