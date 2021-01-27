#coding:utf-8

from time import time
import os

def askCode():
    pwd = input("Please enter the password you want to hack (numbers only) : ")
    while pwd == "":
        pwd = input("Please enter something : ")
    while not pwd.isdigit:
        pwd = input("Please enter numbers only : ")
        while pwd == "":
            pwd = input("Please enter something : ")
    return pwd

def crack(pwd):
    clear()
    length = len(pwd)
    cracked = "0"*length
    crackedint = 0
    t0 = time()
    t1 = time()
    print(f"The password we are trying to hack : {pwd}\n")
    print(f"Number of tries : {cracked}          Elapsed time : 00:00:00", end='')
    while not pwd == cracked:
        crackedint += 1
        cracked = cracked[:length - len(str(crackedint))] + str(crackedint)
        t1 = time()
        t = t1 - t0
        print(f"\rNumber of tries : {cracked}          Elapsed time : {str(int((t)/3600)).zfill(2)}:{str(int((t%3600)/60)).zfill(2)}:{str(int(t%60)).zfill(2)}", end='')
    return t1 - t0  

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == '__main__':
    clear()
    pwd = askCode()
    t = crack(pwd)
    h = int(t/3600)
    m = int((t%3600)/60)
    s = int(t%60)
    finalTime = ""
    if h > 0:
        if h == 1:
            finalTime += f"{h} hour"
        else:
            finalTime += f"{h} hours"
        if m > 0 and s > 0:
            finalTime = ", "
        elif m > 0 or s > 0:
            finalTime = " and "
    if m > 0:
        if m == 1:
            finalTime += f"{m} minute"
        else:
            finalTime += f"{m} minutes"
        if s > 0:
            finalTime += " and "
    if s > 1:
        finalTime += f"{s} seconds"
    elif s == 1:
        finalTime += f"{s} second"


    print(f"\nThe code '{pwd}' has been found in {finalTime} !")