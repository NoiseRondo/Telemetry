import sys


try:
    with open('prov.txt', 'r') as fh:
        lines = [line for line in fh.readlines() if line != '\n']
except IOError as e:
    print(e)
    sys.exit(1)

print(f"В файле строк c текстом:", len(lines))

for line in lines:
    print(f'Строка {line[:50]}... содержит {len(line.split())} слов')
