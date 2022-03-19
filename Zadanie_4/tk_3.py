import sys

zar = 5000

try:
    with open('zarp.txt', 'r') as file:
        stud = file.readlines()
except IOError as e:
    print(e)
    sys.exit(1)

sum_zar = 0

for x in stud:
    name, salary = x.split()

    try:
        salary = float(salary)
    except ValueError:
        continue

    sum_zar += salary
    if salary < zar:
        print(name)

print('Average salary: ', round(sum_zar / len(stud), 2))
