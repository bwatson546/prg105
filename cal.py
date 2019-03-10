fatcal = 0
carcal = 0
procal = 0

def main():
    fg()
    cg()
    pg()
    print("Total Calories: ", float(fatcal) + float(carcal) + float(procal))


def fg():
    global fatcal
    fatg = input("Grams of fat?")
    fatcal = float(fatg)*9
    print("Calories from Fat: ", fatcal)


def cg():
    global carcal
    carg = input("Grams of carbs?")
    carcal = float(carg)*4
    print("Calories from Carbs: ", carcal)


def pg():
    global procal
    prog = input("Grams of protein?")
    procal = float(prog)*4
    print("Calories from Protein: ", procal)

main()
