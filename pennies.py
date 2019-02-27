time = int(input("HOW MUCH TIME HAS BEEN WASTED?"))
print('Days   |\t   Pay')
print('-------------------')
total = 0
penny = 0.01
pay = 0.01

for days in range(time):
    total = total + pay
    print(format(days+1, '6.0f'), "|$\t", format(pay, '7.2f'))
    pay = pay * 2

print("\nYOUR TIME IS WORTH $", format(total, ".2f"))
