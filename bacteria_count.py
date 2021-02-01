"""
Bacteria B replicates itself each 2 minutes, write a program that asks users to enter two numbers,
the initial bacteria number and period of time t(in minutes).Calculate the total number of bacteria
in this period

Test cases:
Input: B=100,t=5
Output: 400

Input: B=100,t=7
Output: 800
"""

import math


def bacteria_count(B, t):
    return int(B) * 2 ** math.floor(int(t) / 2)


b = input("Enter the initial bacteria count:")
t = input("Enter the time(in minutes) to find bacteria count:")
print("The bacteria count after {} minute(s) is:{}".format(t, bacteria_count(b, t)))



