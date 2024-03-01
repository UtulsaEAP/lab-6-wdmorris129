def food_input():
    user_input = input()
    tokens = user_input.split()
    
    # line = "Eating num things a day makes you happy and healthy"
    # Newline = line.replace ("num", tokens[1])
    # Newline = line.replace ("things", tokens[0])

    # print(Newline)
    # print(tokens)

    #type you while  loop here 

    madLib = ["Eating","num","things","a day keeps you happy and healthy."]
    madLib[1] = tokens[1]
    madLib[2] = tokens[0]

    newLine = ' '.join([str(elem) for elem in madLib])

    print(newLine)



    

if __name__ == "__main__":
    food_input()
