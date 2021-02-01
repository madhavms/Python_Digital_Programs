"""
Find the final coordinates of person if the below sequence of 5 turns are repeated:
1)First turns and travels a distance of 10 units
2)Second turn is upwards 20 units
3)Third turn to the left 30 units
4)Fourth turn downwards 40 units
5)Fifth turn right 50 units

Test Cases:
1)Input = 3, Output:-20,20
2)Input = 4, Output:-20,-20
3)Input = 5, Output:30,-20
4)Input = 6, Output:90,-20
"""


def find_coordinate(n):
    x, y = 0, 0
    c = 'R'
    distance = 10
    while n > 0:
        if c == 'R':
            x = x + distance
            distance += 10
            c = 'U'
            n -= 1
        elif c == 'U':
            y = y + distance
            distance += 10
            c = 'L'
            n -= 1
        elif c == 'L':
            x = x - distance
            distance += 10
            c = 'D'
            n -= 1
        elif c == 'D':
            y = y - distance
            distance += 10
            c = 'A'
            n -= 1
        else:
            x = x + distance
            distance += 10
            c = 'R'
            n -= 1

    return [x, y]


a = input("Enter the number of steps to know the coordinates:")
c = find_coordinate(int(a))
print("The final coordinates for {} steps is [{},{}]".format(a,c[0],c[1]))
