"""Will Morris, Friday Afternoon Lab"""

def food_input():
    user_input = input()
    tokens = user_input.split()

    madLib = ["Eating","num","things","a day keeps you happy and healthy."]
    madLib[1] = tokens[1]
    madLib[2] = tokens[0]

    newLine = ' '.join([str(i) for i in madLib])

    print(newLine)


if __name__ == "__main__":
    food_input()
