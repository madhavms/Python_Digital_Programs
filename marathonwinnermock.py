r = []
a = ''

print("Enter the distances covered by the racers in the Marathon(kilometers) please")
print("press q to terminate")

while a != 'q':
    a = input()
    digit = a.isdigit();
    if (not digit) and a != 'q':
        print("Enter a valid number")
        a = 'v'
        continue
    elif a == 'q':
        continue
    elif float(a) > 42.195:
        print("Enter a valid number")
        a = 'v'
        continue

    if a != 'q':
        a = float(a)
        if a > 0.0:
            r.append(a)
        else:
            print("Highest Distance excluding Finishers:")
            print("Invalid Input")

if a != 'v':
    print("Highest Distance excluding Finishers:")
    r = sorted(r, reverse=True)
    count = 0
    for a in r:
        if a != 42.195 and count < 3:
            count += 1
            print(a)


