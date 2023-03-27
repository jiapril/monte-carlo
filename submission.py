# %load "C:\Users\wangj\PycharmProjects\statistics\main.py"
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pi_calculator

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def run_pi(times):
    results={}
    for i in times:
        results[i]=pi_calculator.pi_calculator_np(i)
    print(results)

run_pi([10,100,1000,10000,100000,500000])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
