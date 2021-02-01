# Find the angle between minute hand and the hour hand given the time

def clockangle(s):
    if ':' in s:

        t = s.split(':')
        hh = t[0]
        mm = t[1]

    else:
        print('Enter a valid time in the format hh:mm')
        return -1

    if hh.isdigit() and mm.isdigit():
        hh = int(hh)
        mm = int(mm)
        if 12 < hh < 24:
            hh = hh - 12

        if hh <= 12 and mm < 60:
            hhangle = ((hh * 60) + mm) / 2
            mmangle = mm * 6
            angle = abs(mmangle - hhangle)
            return angle
        else:
            print('Enter a valid time in the format hh:mm')
            return -1
    else:
        print('Enter a valid time in the format hh:mm')
        return -1


a = -1
while a == -1:
    print("Enter the time:")
    time = input()
    a = clockangle(time)
    if a != -1:

        print('The angle between the minute and hour hand for {} is {}°'.format(time, a))
